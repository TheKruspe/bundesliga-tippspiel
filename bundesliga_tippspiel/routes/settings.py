"""LICENSE
Copyright 2017 Hermann Krumrey <hermann@krumreyh.com>

This file is part of bundesliga-tippspiel.

bundesliga-tippspiel is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

bundesliga-tippspiel is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with bundesliga-tippspiel.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

from flask import Blueprint, request, flash, redirect, url_for, \
    make_response, abort, session
from flask_login import login_required, current_user, login_user
from jerrycan.base import db, app
from jerrycan.db.User import User
from jerrycan.enums import AlertSeverity
from bundesliga_tippspiel.Config import Config
from bundesliga_tippspiel.db import Team, UserProfile
from bundesliga_tippspiel.db.settings.DisplayBotsSettings import \
    DisplayBotsSettings
from bundesliga_tippspiel.db.settings.ReminderSettings import \
    ReminderSettings
from bundesliga_tippspiel.enums import ReminderType

import os 
import requests
import secrets
from urllib.parse import urlencode
from datetime import datetime


def format_datetime(value, format='%d.%m.%y'):
    """Convert a float timestamp to a formatted date string."""
    return datetime.fromtimestamp(value).strftime(format)

app.jinja_env.filters['datetime'] = format_datetime


def define_blueprint(blueprint_name: str) -> Blueprint:
    """
    Defines the blueprint for this route
    :param blueprint_name: The name of the blueprint
    :return: The blueprint
    """
    blueprint = Blueprint(blueprint_name, __name__)

    @blueprint.route("/misc_settings", methods=["POST"])
    @login_required
    def misc_settings():
        """
        Allows the user to change their miscellaneous settings
        :return: The response
        """
        setting = DisplayBotsSettings(
            user_id=current_user.id,
            display_bots=request.form.get("display_bots", "off") == "on"
        )
        db.session.merge(setting)
        db.session.commit()

        flash("Einstellungen gespeichert", AlertSeverity.SUCCESS.value)
        return redirect(url_for("user_management.profile"))

    @blueprint.route("/set_reminder", methods=["POST"])
    @login_required
    def set_reminder():
        """
        Allows the user to set an email reminder
        :return: The response
        """
        hours = int(request.form["hours"])
        reminder_states = {
            reminder_type:
                request.form.get(reminder_type.value) in ["on", True]
            for reminder_type in ReminderType
        }

        if not 0 < hours < 49:
            flash("Ungültige Anzahl Stunden eingegeben", "danger")
        else:
            for reminder_type, reminder_state in reminder_states.items():
                setting = ReminderSettings(
                    user_id=current_user.id,
                    reminder_type=reminder_type,
                    active=reminder_state,
                    reminder_time=hours
                )
                db.session.merge(setting)
            db.session.commit()
            flash("Erinnerungseinstellungen gespeichert", "success")

        return redirect(url_for("user_management.profile"))

    @blueprint.route("/change_league", methods=["GET"])
    @login_required
    def change_league():
        """
        Changes the user's currently displayed league by storing these
        values in a cookie
        :return: None
        """
        try:
            league = request.args.get("league", Config.OPENLIGADB_LEAGUE)
            season = request.args.get("season", Config.OPENLIGADB_SEASON)
            int(season)
        except ValueError:
            return abort(400)
        app.logger.info(request.referrer)
        response = make_response(redirect(url_for("betting.get_current_bets")))
        response.set_cookie("league", league)
        response.set_cookie("season", season)
        return response

    @blueprint.route("/set_profile_info", methods=["POST"])
    @login_required
    def set_profile_info():
        """
        Sets the profile info for a user
        :return: The response
        """
        team_names = [x.abbreviation for x in Team.query.all()]

        description = request.form.get("about_me")
        favourite_team = request.form.get("favourite_team")
        if not description:
            description = None
        if favourite_team not in team_names:
            favourite_team = None
        country = None

        profile_info = UserProfile(
            user_id=current_user.id,
            description=description,
            favourite_team_abbreviation=favourite_team,
            country=country
        )
        db.session.merge(profile_info)
        db.session.commit()
        return redirect(url_for("user_management.profile"))
    
    @blueprint.route('/callback/<provider>')
    def oauth2_callback(provider):
        if not current_user.is_anonymous:
            return redirect(url_for('static.index'))

        provider_data = Config.OAUTH2_PROVIDERS.get(provider)
        if provider_data is None:
            abort(404)

        # if there was an authentication error, flash the error messages and exit
        if 'error' in request.args:
            for k, v in request.args.items():
                if k.startswith('error'):
                    flash(f'{k}: {v}')
            return redirect(url_for('static.index'))
        # make sure that the state parameter matches the one we created in the
        # authorization request
        if request.args['state'] != session.get('oauth2_state'):
            abort(401)

        # make sure that the authorization code is present
        if 'code' not in request.args:
            abort(401)

        # exchange the authorization code for an access token
        response = requests.post(provider_data['token_url'], data={
            'client_id': provider_data['client_id'],
            'client_secret': provider_data['client_secret'],
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': url_for('settings.oauth2_callback', provider=provider,
                                    _external=True, _scheme='https'),
        }, headers={'Accept': 'application/json'})
        if response.status_code != 200:
            abort(401)
        oauth2_token = response.json().get('access_token')
        if not oauth2_token:
            abort(401)

        # use the access token to get the user's email address
        response = requests.get(provider_data['userinfo']['url'], headers={
            'Authorization': 'Bearer ' + oauth2_token,
            'Accept': 'application/json',
        })
        if response.status_code != 200:
            abort(401)
        email = provider_data['userinfo']['email'](response.json())

        # app.logger.info("PROVIDER DATA - USER INFO", provider_data["userinfo"])

        # find or create the user in the database
        user = db.session.scalar(db.select(User).where(User.email == email))
        if user is None:
            user = User(email=email, username=email.split('@')[0], confirmed=True)
            db.session.add(user)
            db.session.commit()

        # log the user in
        login_user(user)
        return redirect(url_for('static.index'))

    @blueprint.route('/authorize/<provider>')
    def oauth2_authorize(provider):
        if not current_user.is_anonymous:
            return redirect(url_for('static.index'))

        provider_data = Config.OAUTH2_PROVIDERS.get(provider)
        if provider_data is None:
            abort(404)

        # generate a random string for the state parameter
        session['oauth2_state'] = secrets.token_urlsafe(16)

        # create a query string with all the OAuth2 parameters
        qs = urlencode({
            'client_id': provider_data['client_id'],
            'redirect_uri': url_for('settings.oauth2_callback', provider=provider,
                                    _external=True, _scheme='https'),
            'response_type': 'code',
            'scope': ' '.join(provider_data['scopes']),
            'state': session['oauth2_state'],
        })

        # redirect the user to the OAuth2 provider authorization URL
        return redirect(provider_data['authorize_url'] + '?' + qs)

    return blueprint
