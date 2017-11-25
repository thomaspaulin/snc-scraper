import snc.scraper.parsing_utils as util
from snc.scraper.team import Team
from snc.scraper.division import Division

"""
# For parsing
http://www.aucklandsnchockey.com/leagues/teams.cfm?leagueID=23341&clientID=5788
"""


def parse_name(name_wrapper_elem):
    return name_wrapper_elem.select('span')[0].contents[0]


def parse_logo(img_wrapper_elem):
    base_url = 'http://www.aucklandsnchockey.com/'
    src = img_wrapper_elem.select('img')[0]['src']
    return base_url + src


def parse_record(record_wrapper_elem):
    """Returns the parsed team record as a tuple in the form W-L-T"""
    records = record_wrapper_elem.contents[2].split('-')
    return int(records[0]), int(records[1]), int(records[2])


def parse_team(team_elem, division):
    rows = team_elem.select('tr')
    # row 1 is logo, name, and links to stats, roster, and staff/personnel
    name = util.capitalise(parse_name(rows[0].select('td')[1]))
    logo_url = parse_logo(rows[0].select('td')[0])
    # row 2 is current record and next home game
    record = parse_record(rows[1].select('td')[1])
    # row 3 onwards are the awards and special notes including the title and a
    # row for an empty div
    return Team(name=name,
                division=division,
                logo_url=logo_url,
                record=record)


def parse_division(header_elem):
    """Returns the division parsed from the team page section header"""
    title = header_elem.select('b')[0].contents[0]
    # title should look like `SNC - B League Competition`
    return Division(name=title.split('-')[1].strip()[0:1])


def parse(soup):
    """Returns the teams in the league that could be parsed"""
    parsed_teams = []
    team_elems = soup.select('div > table.boxscores')[1:]
    current_division = Division(name='Unknown')
    for elem in team_elems:
        if len(elem.select('font')) is not 0:
            current_division = parse_division(elem)
        else:
            parsed_teams.append(parse_team(elem, current_division))
    return parsed_teams
