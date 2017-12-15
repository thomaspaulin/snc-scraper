from typing import Dict, List

import cloudinary.uploader
import requests

import snc.scraper.parsing_utils as util
from snc.scraper.constants import BASE_URL
from snc.scraper.division import Division
from snc.scraper.team import Team

"""
# For parsing
http://www.aucklandsnchockey.com/leagues/teams.cfm?leagueID=23341&clientID=5788
"""


def parse_name(name_wrapper_elem) -> str:
    return str(name_wrapper_elem.select('span')[0].contents[0])


def parse_logo(img_wrapper_elem) -> str:
    base_url = BASE_URL
    src = img_wrapper_elem.select('img')[0]['src']
    return str(base_url + src)


def parse_record(record_wrapper_elem) -> (int, int, int):
    """Returns the parsed team record as a tuple in the form W-L-T"""
    records = record_wrapper_elem.contents[2].split('-')
    return int(records[0]), int(records[1]), int(records[2])


def parse_team(team_elem, division_name: str, known_teams: Dict[str, Team]) -> Team:
    rows = team_elem.select('tr')
    # row 1 is logo, name, and links to stats, roster, and staff/personnel
    name: str = util.capitalise(parse_name(rows[0].select('td')[1]))
    try:
        return known_teams[name.lower()]
    except KeyError:
        print("The server does not know about team {}.".format(name))
    logo_url = parse_logo(rows[0].select('td')[0])
    # row 2 is current record and next home game
    record = parse_record(rows[1].select('td')[1])
    # row 3 onwards are the awards and special notes including the title and a
    # row for an empty div

    url = cloudinary.CloudinaryImage('team-logos/' + name.lower()).url
    res = requests.head(url)
    if res.status_code == 404:
        url = cloudinary.uploader.upload(logo_url, public_id=str('team-logos/' + name.lower()))['url']
    return Team(name=name, division_name=division_name, logo_url=url, record=record)


def parse_division(header_elem, known_divisions: Dict[str, Division]) -> Division:
    """Returns the division parsed from the team page section header"""
    title: str = str(header_elem.select('b')[0].contents[0]).strip()
    try:
        header_elem.select('td')[0].contents[0].contents[0].startswith('Division:')
    except AttributeError:
        return Division(name='Unknown')
    # title should look like `SNC - B League Competition` for SNC
    #                        `BHL - BACKYARD HOCKEY LEAGUE` for BHL
    #                        `FHL - FRONTYARD HOCKEY LEAGUE` for FHL
    div_title = title.split('-')
    if div_title[0].strip() == 'SNC':
        name: str = str(div_title[1].strip()[0:1]).strip()
    elif div_title[0].strip() == 'BHL' or div_title[0].strip() == 'FHL':
        name: str = str(div_title[0]).strip()
    else:
        return Division(name='Unknown')

    try:
        return known_divisions[name.lower()]
    except KeyError:
        print("The server does not know about division {}.".format(name))
    return Division(name=name)


def parse(soup, known_teams: Dict[str, Team], known_divisions: Dict[str, Division]) -> List[Team]:
    """Returns the teams in the league that could be parsed"""
    parsed_teams = []
    team_elems = soup.select('div > table.boxscores')
    current_division = Division(name='Unknown')
    for elem in team_elems:
        if len(elem.select('font')) is not 0:
            current_division = parse_division(elem, known_divisions)
        else:
            parsed_teams.append(parse_team(elem, current_division.name, known_teams))
    return parsed_teams
