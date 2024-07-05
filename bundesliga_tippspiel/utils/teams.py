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

from typing import Tuple


def get_team_data(team_name: str) -> Tuple[str, str, str, Tuple[str, str]]:
    """
    Generates team short_names, abbreviations and icon URLs for teams
    :param team_name: The team's full name as specified by OpenLigaDB
    :return: A tuple containing the
            name, short_name, abbreviation, svg URL, png URL
    """
    # Tuples: abbrv: openligadb name, full name, short name, logos
    team_map = {
        "FCN": (
            "1. FC Nürnberg", "1. FC Nürnberg", "1. FC Nürnberg",
            wikimedia_icon_urls("commons/f/fa/1._FC_Nürnberg_logo.svg")
        ),
        "M05": (
            "1. FSV Mainz 05", "1. FSV Mainz 05", "FSV Mainz 05",
            wikimedia_icon_urls("commons/0/0b/FSV_Mainz_05_Logo.svg")
        ),
        "B04": (
            "Bayer Leverkusen", "Bayer 04 Leverkusen", "Bayer Leverkusen",
            wikimedia_icon_urls("de/f/f7/Bayer_Leverkusen_Logo.svg")
        ),
        "BVB": (
            "Borussia Dortmund", "Borussia Dortmund", "BVB Dortmund",
            wikimedia_icon_urls("commons/6/67/Borussia_Dortmund_logo.svg")
        ),
        "BMG": (
            "Borussia Mönchengladbach", "Borussia Mönchengladbach",
            "M'Gladbach", wikimedia_icon_urls("commons/8/81/Borussia_"
                                              "Mönchengladbach_logo.svg")
        ),
        "SGE": (
            "Eintracht Frankfurt", "Eintracht Frankfurt", "Frankfurt",
            wikimedia_icon_urls("commons/0/04/Eintracht_Frankfurt_Logo.svg")
        ),
        "FCA": (
            "FC Augsburg", "FC Augsburg", "FC Augsburg",
            wikimedia_icon_urls("de/b/b5/Logo_FC_Augsburg.svg")
        ),
        "FCB": (
            "FC Bayern München", "FC Bayern München", "FC Bayern",
            wikimedia_icon_urls("commons/1/1b/"
                                "FC_Bayern_München_logo_(2017).svg")
        ),
        "S04": (
            "FC Schalke 04", "FC Schalke 04", "Schalke 04",
            wikimedia_icon_urls("commons/6/6d/FC_Schalke_04_Logo.svg")
        ),
        "F95": (
            "Fortuna Düsseldorf", "Fortuna Düsseldorf", "Düsseldorf",
            wikimedia_icon_urls("commons/9/94/Fortuna_D%C3%BCsseldorf.svg")
        ),
        "H96": (
            "Hannover 96", "Hannover 96", "Hannover 96",
            wikimedia_icon_urls("commons/c/cd/Hannover_96_Logo.svg")
        ),
        "BSC": (
            "Hertha BSC", "Hertha BSC Berlin", "Hertha BSC",
            wikimedia_icon_urls("commons/8/81/Hertha_BSC_Logo_2012.svg")
        ),
        "RBL": (
            "RB Leipzig", "RB Leibzig", "RB Leibzig",
            wikimedia_icon_urls("it/c/cc/RB_Leipzig_primo_logo.svg")
        ),
        "SCF": (
            "SC Freiburg", "SC Freiburg", "SC Freiburg",
            wikimedia_icon_urls("de/b/bf/SC_Freiburg_Logo.svg")
        ),
        "SVEB": (
            "SV Elversberg 07", "SV Elversberg 07", "SV Elversberg",
            wikimedia_icon_urls("commons/d/d4/SV_Elversberg_Logo_2021.svg")
        ),
        "TSG": (
            "TSG 1899 Hoffenheim", "TSG 1899 Hoffenheim", "TSG Hoffenheim",
            wikimedia_icon_urls("commons/e/e7/Logo_TSG_Hoffenheim.svg")
        ),
        "VFB": (
            "VfB Stuttgart", "VFB Stuttgart", "VFB Stuttgart",
            wikimedia_icon_urls("commons/e/eb/VfB_Stuttgart_1893_Logo.svg")
        ),
        "WOB": (
            "VfL Wolfsburg", "VFL Wolfsburg", "VFL Wolfsburg",
            wikimedia_icon_urls("commons/c/ce/VfL_Wolfsburg_Logo.svg")
        ),
        "BRE": (
            "Werder Bremen", "SV Werder Bremen", "Werder Bremen",
            wikimedia_icon_urls("commons/b/be/SV-Werder-Bremen-Logo.svg")
        ),
        "FCU": (
            "1. FC Union Berlin", "1. FC Union Berlin", "Union Berlin",
            wikimedia_icon_urls("fr/0/0a/1._FC_Union_Berlin_-_Logo.svg")
        ),
        "SCP": (
            "SC Paderborn 07", "SC Paderborn 07", "Paderborn",
            wikimedia_icon_urls("en/b/b3/SC_Paderborn_07_logo.svg")
        ),
        "KOE": (
            "1. FC Köln", "1. FC Köln", "1. FC Köln",
            wikimedia_icon_urls("commons/0/01/1._FC_Koeln_Logo_2014–.svg")
        ),
        "DSC": (
            "Arminia Bielefeld", "Arminia Bielefeld", "Bielefeld",
            wikimedia_icon_urls("commons/2/26/Arminia-wappen-2021.svg")
        ),
        "SGF": (
            "SpVgg Greuther Fürth", "SpVgg Greuther Fürth", "Greuther Fürth",
            wikimedia_icon_urls("commons/b/b1/SpVgg_Greuther_Fürth_2017.svg")
        ),
        "BOC": (
            "VfL Bochum", "VfL Bochum", "VfL Bochum",
            wikimedia_icon_urls("commons/7/72/VfL_Bochum_logo.svg")
        ),
        "HDH": (
            "1. FC Heidenheim 1846", "1. FC Heidenheim", "Heidenheim",
            wikimedia_icon_urls("commons/9/9d/1._FC_Heidenheim_1846.svg")
        ),
        "AUE": (
            "Erzgebirge Aue", "Erzgebirge Aue", "Erzgebirge Aue",
            wikimedia_icon_urls("en/9/9e/FC_Erzgebirge_Aue_logo.svg")
        ),
        "FCH": (
            "FC Hansa Rostock", "FC Hansa Rostock", "Hansa Rostock",
            wikimedia_icon_urls("commons/8/8f/F.C._Hansa_Rostock_Logo.svg")
        ),
        "FCI": (
            "FC Ingolstadt 04", "FC Ingolstadt 04", "FC Ingolstadt",
            wikimedia_icon_urls("en/0/0b/FC_Ingolstadt_04_logo.svg")
        ),
        "STP": (
            "FC St. Pauli", "FC St. Pauli", "St. Pauli",
            wikimedia_icon_urls("en/8/8f/FC_St._Pauli_logo_%282018%29.svg")
        ),
        "HSV": (
            "Hamburger SV", "Hamburger SV", "Hamburger SV",
            wikimedia_icon_urls("commons/f/f7/Hamburger_SV_logo.svg")
        ),
        "KIE": (
            "Holstein Kiel", "Holstein Kiel", "Holstein Kiel",
            wikimedia_icon_urls("commons/3/30/Holstein_Kiel_Logo.svg")
        ),
        "SSV": (
            "Jahn Regensburg", "SSV Jahn Regensburg", "Jahn Regensburg",
            wikimedia_icon_urls("commons/3/3d/Jahn_Regensburg_logo2014.svg")
        ),
        "KSC": (
            "Karlsruher SC", "Karlsruher SC", "Karlsruher SC",
            wikimedia_icon_urls("commons/c/c8/Karlsruher_SC_Logo_2.svg")
        ),
        "SGD": (
            "SG Dynamo Dresden", "SG Dynamo Dresden", "Dynamo Dresden",
            wikimedia_icon_urls("en/0/06/Dynamo_Dresden_logo_2011.svg")
        ),
        "D98": (
            "SV Darmstadt 98", "SV Darmstadt 98", "SV Darmstadt",
            wikimedia_icon_urls("en/9/92/SV_Darmstadt_98_logo.svg")
        ),
        "SVS": (
            "SV Sandhausen", "SV Sandhausen", "SV Sandhausen",
            wikimedia_icon_urls("commons/d/d3/SV_Sandhausen.svg")
        ),
        "FCK": (
            "1. FC Kaiserslautern", "1. FC Kaiserslautern", "Kaiserslautern",
            wikimedia_icon_urls("commons/d/d3/Logo_1_FC_Kaiserslautern.svg")
        ),
        "FCM": (
            "1. FC Magdeburg", "1. FC Magdeburg", "Magdeburg",
            wikimedia_icon_urls("commons/8/84/1._FC_Magdeburg.svg")
        ),
        "FCS": (
            "1. FC Saarbrücken", "1. FC Saarbrücken", "Saarbrücken",
            wikimedia_icon_urls("de/f/ff/1._FC_Saarbr%C3%BCcken.svg")
        ),
        "BRA": (
            "Eintracht Braunschweig", "Eintracht Braunschweig", "Braunschweig",
            wikimedia_icon_urls("de/4/45/Logo_Eintracht_Braunschweig.svg")
        ),
        "VBE": (
            "FC Viktoria 1889 Berlin", "FC Viktoria Berlin", "Viktoria Berlin",
            wikimedia_icon_urls(
                "commons/4/40/FC_Viktoria_1889_Berlin_Logo.svg")
        ),
        "VKO": (
            "FC Viktoria Köln", "FC Viktoria Köln", "Viktoria Köln",
            wikimedia_icon_urls(
                "commons/d/dc/FC_Viktoria_K%C3%B6ln_1904_Logo.svg")
        ),
        "HFC": (
            "Hallescher FC", "Hallescher FC", "Halle",
            wikimedia_icon_urls("commons/e/e1/Hallescher_FC.svg")
        ),
        "MSV": (
            "MSV Duisburg", "MSV Duisburg", "Duisburg",
            wikimedia_icon_urls("commons/0/02/Msv_duisburg_%282017%29.svg")
        ),
        "SC2": (
            "SC Freiburg II", "SC Freiburg II", "Freiburg II",
            wikimedia_icon_urls("de/8/88/Logo-SC_Freiburg.svg")
        ),
        "SCV": (
            "SC Verl", "SC Verl", "Verl",
            wikimedia_icon_urls("commons/c/ce/SC_Verl_Logo.svg")
        ),
        "SVM": (
            "SV Meppen", "SV Meppen", "Meppen",
            wikimedia_icon_urls("commons/4/45/Logo_SV_Meppen_2019.svg")
        ),
        "MAN": (
            "SV Waldhof Mannheim", "SV Waldhof Mannheim", "Mannheim",
            wikimedia_icon_urls("commons/1/1c/SV_Waldhof_Mannheim_Wappen.svg")
        ),
        "WIE": (
            "SV Wehen Wiesbaden", "SV Wehen Wiesbaden", "Wiesbaden",
            wikimedia_icon_urls("de/3/3d/Logo_SV_Wehen_Wiesbaden.svg")
        ),
        "MÜN": (
            "TSV 1860 München", "TSV 1860 München", "1860 München",
            wikimedia_icon_urls("commons/4/48/TSV_1860_M%C3%BCnchen.svg")
        ),
        "HAV": (
            "TSV Havelse", "TSV Havelse", "Havelse",
            wikimedia_icon_urls("commons/8/89/TSV_Havelse_logo.svg")
        ),
        "TÜR": (
            "Türkgücü München", "Türkgücü München", "Türkgücü",
            wikimedia_icon_urls("commons/f/fe/T%C3%BCrkg%C3%BCc%C3%BC_"
                                "M%C3%BCnchen_Logo.svg")
        ),
        "OSN": (
            "VfL Osnabrück", "VfL Osnabrück", "Osnabrück",
            wikimedia_icon_urls(
                "commons/4/4e/VfL_Osnabrueck_Logo_2021–.svg")
        ),
        "WÜR": (
            "Würzburger Kickers", "Würzburger Kickers", "Würzburg",
            wikimedia_icon_urls(
                "commons/0/0c/W%C3%BCrzburger_Kickers_Logo.svg")
        ),
        "BV2": (
            "Borussia Dortmund II", "Borussia Dortmund II", "Dortmund II",
            wikimedia_icon_urls("commons/6/67/Borussia_Dortmund_logo.svg")
        ),
        "ZWI": (
            "FSV Zwickau", "FSV Zwickau", "Zwickau",
            wikimedia_icon_urls("de/0/01/FSV_Zwickau_Logo.svg")
        ),
        "PHL": (
            "1. FC Phönix Lübeck", "1. FC Phönix Lübeck", "Phönix Lübeck",
            wikimedia_icon_urls("commons/9/9b/1._FC_Phoenix_Luebeck_Logo.svg")
        ),
        "AAA": (
            "Alemannia Aachen", "Alemannia Aachen", "Aachen",
            wikimedia_icon_urls("de/7/76/Logo_Alemannia_Aachen.svg")
        ),
        "BSV": (
            "Bremer SV", "Bremer SV", "Bremer SV",
            wikimedia_icon_urls("commons/a/a7/Bremer_SV_Logo.png")
        ),
        "FCV": (
            "FC 08 Villingen", "FC 08 Villingen", "Villingen",
            wikimedia_icon_urls("de/5/55/FC_08_Villingen.svg")
        ),
        "CZJ": (
            "FC Carl Zeiss Jena", "FC Carl Zeiss Jena", "Jena",
            wikimedia_icon_urls("commons/e/e4/Logo_FC_Carl_Zeiss_Jena.svg")
        ),
        "ENC": (
            "FC Energie Cottbus", "FC Energie Cottbus", "Cottbus",
            wikimedia_icon_urls("commons/5/55/Logo_Energie_Cottbus.svg")
        ),
        "GFC": (
            "Greifswalder FC", "Greifswalder FC", "Greifswald",
            wikimedia_icon_urls("commons/f/f6/Greifswalder_FC_Logo.svg")
        ),
        "KOF": (
            "Kickers Offenbach", "Kickers Offenbach", "Offenbach",
            wikimedia_icon_urls("de/f/f9/Logo_Kickers_Offenbach.svg")
        ),
        "PMÜ": (
            "Preußen Münster", "Preußen Münster", "Münster",
            wikimedia_icon_urls("de/7/7e/SC_Preussen_Muenster_Logo_2018.svg")
        ),
        "RWE": (
            "Rot-Weiss Essen", "Rot-Weiss Essen", "Essen",
            wikimedia_icon_urls("de/8/8a/Logo_Rot-Weiss_Essen.svg")
        ),
        "SFL": (
            "Sportfreunde Lotte", "Sportfreunde Lotte", "Lotte",
            wikimedia_icon_urls("commons/6/6f/Logo_SF_Lotte.svg")
        ),
        "SVU": (
            "SSV Ulm 1846", "SSV Ulm 1846", "Ulm",
            wikimedia_icon_urls("commons/6/6c/SSV_Ulm_1846_Fussball.svg")
        ),
        "TOT": (
            "Teutonia Ottensen", "Teutonia Ottensen", "Ottensen",
            wikimedia_icon_urls("commons/f/f3/FC_Teutonia_05_Ottensen_Logo.svg")
        ),
        "TSM": (
            "TSV Schott Mainz", "TSV Schott Mainz", "Mainz",
            wikimedia_icon_urls("commons/4/48/TSV_Schott_Mainz.png")
        ),
        "TUS": (
            "TuS Koblenz", "TuS Koblenz", "Koblenz",
            wikimedia_icon_urls("commons/0/04/TuS_Koblenz.svg")
        ),
        "VAL": (
            "VfR Aalen", "VfR Aalen", "Aalen",
            wikimedia_icon_urls("commons/2/2f/VfR_Aalen_Wappen.svg")
        ),
        "VFV": (
            "VfV 06 Hildesheim", "VfV 06 Hildesheim", "Hildesheim",
            wikimedia_icon_urls("de/7/74/VfV_06_Hildesheim_Logo.svg")
        ),
    }

    def wikimedia_flag_urls(path):
        return wikimedia_icon_urls(path)
        return f"https://upload.wikimedia.org/wikipedia/{path}"

    country_map = {
        "GER": ("Deutschland", "Deutschland", "Deutschland", wikimedia_flag_urls("commons/b/ba/Flag_of_Germany.svg")),
        "FRA": ("Frankreich", "Frankreich", "Frankreich", wikimedia_flag_urls("commons/c/c3/Flag_of_France.svg")),
        "ITA": ("Italien", "Italien", "Italien", wikimedia_flag_urls("commons/0/03/Flag_of_Italy.svg")),
        "ESP": ("Spanien", "Spanien", "Spanien", wikimedia_flag_urls("commons/9/9a/Flag_of_Spain.svg")),
        "POR": ("Portugal", "Portugal", "Portugal", wikimedia_flag_urls("commons/5/5c/Flag_of_Portugal.svg")),
        "NED": ("Niederlande", "Niederlande", "Niederlande", wikimedia_flag_urls("commons/2/20/Flag_of_the_Netherlands.svg")),
        "BEL": ("Belgien", "Belgien", "Belgien", wikimedia_flag_urls("commons/6/65/Flag_of_Belgium.svg")),
        "ENG": ("England", "England", "England", wikimedia_flag_urls("commons/b/be/Flag_of_England.svg")),
        "SCO": ("Schottland", "Schottland", "Schottland", wikimedia_flag_urls("commons/1/10/Flag_of_Scotland.svg")),
        "WAL": ("Wales", "Wales", "Wales", wikimedia_flag_urls("commons/5/59/Flag_of_Wales_2.svg")),
        "IRL": ("Irland", "Irland", "Irland", wikimedia_flag_urls("commons/4/45/Flag_of_Ireland.svg")),
        "NIR": ("Nordirland", "Nordirland", "Nordirland", wikimedia_flag_urls("commons/d/d4/Flag_of_Northern_Ireland.svg")),
        "SWE": ("Schweden", "Schweden", "Schweden", wikimedia_flag_urls("commons/4/4c/Flag_of_Sweden.svg")),
        "NOR": ("Norwegen", "Norwegen", "Norwegen", wikimedia_flag_urls("commons/d/d9/Flag_of_Norway.svg")),
        "DEN": ("Dänemark", "Dänemark", "Dänemark", wikimedia_flag_urls("commons/9/9c/Flag_of_Denmark.svg")),
        "FIN": ("Finnland", "Finnland", "Finnland", wikimedia_flag_urls("commons/b/bc/Flag_of_Finland.svg")),
        "POL": ("Polen", "Polen", "Polen", wikimedia_flag_urls("commons/1/12/Flag_of_Poland.svg")),
        "CZE": ("Tschechien", "Tschechien", "Tschechischen", wikimedia_flag_urls("commons/c/cb/Flag_of_the_Czech_Republic.svg")),
        "SUI": ("Schweiz", "Schweiz", "Schweiz", wikimedia_flag_urls("commons/f/f3/Flag_of_Switzerland.svg")),
        "AUT": ("Österreich", "Österreich", "Österreich", wikimedia_flag_urls("commons/4/41/Flag_of_Austria.svg")),
        "RUS": ("Russland", "Russland", "Russland", wikimedia_flag_urls("commons/f/f3/Flag_of_Russia.svg")),
        "UKR": ("Ukraine", "Ukraine", "Ukraine", wikimedia_flag_urls("commons/4/49/Flag_of_Ukraine.svg")),
        "CRO": ("Kroatien", "Kroatien", "Kroatien", wikimedia_flag_urls("commons/1/1b/Flag_of_Croatia.svg")),
        "SRB": ("Serbien", "Serbien", "Serbien", wikimedia_flag_urls("commons/f/ff/Flag_of_Serbia.svg")),
        "BIH": ("Bosnien und Herzegowina", "Bosnien und Herzegowina", "Bosnien und Herzegowina", wikimedia_flag_urls("commons/b/bf/Flag_of_Bosnia_and_Herzegovina.svg")),
        "MNE": ("Montenegro", "Montenegro", "Montenegro", wikimedia_flag_urls("commons/6/64/Flag_of_Montenegro.svg")),
        "MKD": ("Nordmazedonien", "Nordmazedonien", "Nordmazedonien", wikimedia_flag_urls("commons/f/f8/Flag_of_North_Macedonia.svg")),
        "ALB": ("Albanien", "Albanien", "Albanien", wikimedia_flag_urls("commons/3/36/Flag_of_Albania.svg")),
        "GRE": ("Griechenland", "Griechenland", "Griechenland", wikimedia_flag_urls("commons/5/5c/Flag_of_Greece.svg")),
        "BUL": ("Bulgarien", "Bulgarien", "Bulgarien", wikimedia_flag_urls("commons/9/9a/Flag_of_Bulgaria.svg")),
        "ROU": ("Rumänien", "Rumänien", "Rumänien", wikimedia_flag_urls("commons/7/73/Flag_of_Romania.svg")),
        "HUN": ("Ungarn", "Ungarn", "Ungarn", wikimedia_flag_urls("commons/c/c1/Flag_of_Hungary.svg")),
        "SVK": ("Slowakei", "Slowakei", "Slowakei", wikimedia_flag_urls("commons/e/e6/Flag_of_Slovakia.svg")),
        "SLO": ("Slowenien", "Slowenien", "Slowenien", wikimedia_flag_urls("commons/f/f0/Flag_of_Slovenia.svg")),
        "BLR": ("Weißrussland", "Weißrussland", "Weißrussland", wikimedia_flag_urls("commons/8/85/Flag_of_Belarus.svg")),
        "LTU": ("Litauen", "Litauen", "Litauen", wikimedia_flag_urls("commons/1/11/Flag_of_Lithuania.svg")),
        "LVA": ("Lettland", "Lettland", "Lettland", wikimedia_flag_urls("commons/8/84/Flag_of_Latvia.svg")),
        "EST": ("Estland", "Estland", "Estland", wikimedia_flag_urls("commons/8/8f/Flag_of_Estonia.svg")),
        "MDA": ("Moldawien", "Moldawien", "Moldawien", wikimedia_flag_urls("commons/2/27/Flag_of_Moldova.svg")),
        "ARM": ("Armenien", "Armenien", "Armenien", wikimedia_flag_urls("commons/2/2f/Flag_of_Armenia.svg")),
        "GEO": ("Georgien", "Georgien", "Georgien", wikimedia_flag_urls("commons/0/0f/Flag_of_Georgia.svg")),
        "AZE": ("Aserbaidschan", "Aserbaidschan", "Aserbaidschan", wikimedia_flag_urls("commons/d/dd/Flag_of_Azerbaijan.svg")),
        "KAZ": ("Kasachstan", "Kasachstan", "Kasachstan", wikimedia_flag_urls("commons/d/d3/Flag_of_Kazakhstan.svg")),
        "TUR": ("Türkei", "Türkei", "Türkei", wikimedia_flag_urls("commons/b/b4/Flag_of_Turkey.svg")),
        "CYP": ("Zypern", "Zypern", "Zypern", wikimedia_flag_urls("commons/d/d4/Flag_of_Cyprus.svg")),
        "ISR": ("Israel", "Israel", "Israel", wikimedia_flag_urls("commons/d/d4/Flag_of_Israel.svg")),
        "NO": ("noch offen", "noch offen", "noch offen", wikimedia_flag_urls("commons/d/d4/Flag_of_Israel.svg")),
    }

    openligadb_map = {
        info[0]: (
            info[1],
            info[2],
            abbreviation,
            info[3]
        )
        for abbreviation, info in list(team_map.items()) + list(country_map.items())
    }
    return openligadb_map[team_name]


def wikimedia_icon_urls(path: str, png_size: int = 500) -> Tuple[str, str]:
    """
    Generates URL paths to wikimedia-hosted SVG and PNG files
    :param path: The URL path to the SVG file (without the wikimedia part)
    :param png_size: The size of the PNG file
    :return: The URL path to the SVG File, PNG file
    """
    wikimedia = "https://upload.wikimedia.org/wikipedia"
    base, specific = path.split("/", 1)
    svg_filename = path.rsplit("/", 1)[1]

    svg_url = "{}/{}".format(wikimedia, path)
    png_url = "{}/{}/thumb/{}/{}px-{}.png".format(
        wikimedia, base, specific, png_size, svg_filename
    )

    return svg_url, png_url
