<?php
/*  Copyright Hermann Krumrey <hermann@krumreyh.com> 2017

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
*/

/**
 * Generates a german dictionary
 * @return array: the german dictionary
 */
function get_german() {
    return array(

        # NAVBAR TITLES
        'WEBSITE_NAME' => 'Bundesliga Tippspiel',
        'HOME_NAV_TITLE' => 'Home',
        'LOGIN_NAV_TITLE' => 'Anmelden',
        'THEMES_NAV_TITLE' => 'Themen',
        'THEME_DEFAULT_NAV_TITLE' => 'Standard',
        'THEME_TERMINAL_NAV_TITLE' => 'Konsole',
        'LANGUAGES_NAV_TITLE' => 'Sprachen',
        'LANGUAGE_GERMAN_NAV_TITLE' => 'Deutsch',
        'LANGUAGE_ENGLISH_NAV_TITLE' => 'Englisch',
        'FOOTER_IMPRESSUM_TITLE' => 'Impressum',
        'FOOTER_COPYRIGHT_TEXT' => '© Hermann Krumrey 2017',
        'FOOTER_VERSION_TEXT' => '0.1.0'
    );
}