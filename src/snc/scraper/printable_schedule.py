import bs4

from snc.scraper.match import Match, MatchType
from snc.scraper.parsing_utils import parse_schedule_date
from snc.scraper.rink import Rink
from snc.scraper.teams import Team

"""
For parsing
http://www.aucklandsnchockey.com/leagues/print_schedule.cfm?leagueID=23341&clientID=5788&teamID=0&mixed=1
"""


def parse_score(score_elem):
    """Returns the score parsed from the provided bs4 Tag or -1 if there
    wasn't one"""
    if isinstance(score_elem, bs4.element.Tag):
        score_elem = score_elem.contents[0]
    try:
        return int(score_elem.strip())
    except ValueError:
        try:
            # team won in overtime or shootout so trim off the 'OT' or 'SO'
            return int(score_elem.strip()[:-2].strip())
        except ValueError:
            # no score
            return -1


def parse_team(team_elem, known_teams):
    """Returns the team name parsed from the provided bs4 Tag"""
    if isinstance(team_elem, bs4.element.Tag):
        team_elem = team_elem.contents[0]
    try:
        name = team_elem.strip()
    except TypeError:
        name = team_elem.select('b')[0].contents[0].strip()
    try:
        return known_teams[name.lower()]
    except KeyError:
        print("The server does not know about team {}.".format(name))
        return Team(name=name,
                    division_name='Unknown')


def parse_rink(rink_elem):
    if isinstance(rink_elem, bs4.element.Tag):
        rink_elem = rink_elem.contents[0]
    return rink_elem.strip()[:-5]


game_type = {
    'PR': MatchType.PRACTICE,
    'RS': MatchType.REGULAR_SEASON,
    'PO': MatchType.PLAYOFF
}


def parse_row(row_elem, known_teams):
    tds = row_elem.select('td')

    # Playoff rows have these header ones before them to indicate which
    # game they are
    is_match_row = len(tds[0].select('img')) is 0
    if is_match_row:
        game_type_acronym = tds[0].select('font')[0].contents[0].strip()

        # In the format SA 18-Mar-2017 4:30P
        date = parse_schedule_date(tds[1].contents[0].strip() + ' ' + tds[2].contents[0].strip())
        # practice and regular season
        away = parse_team(tds[3].contents[0], known_teams)
        away_score = parse_score(tds[4].contents[0])
        home = parse_team(tds[5].contents[0], known_teams)
        home_score = parse_score(tds[6].contents[0])
        rink = Rink(name=parse_rink(tds[7].contents[0]))

        return Match(game_type=game_type[game_type_acronym],
                     season=date.year,
                     start=date,
                     away=away,
                     home=home,
                     away_score=away_score,
                     home_score=home_score,
                     rink=rink)
    else:
        return None


def parse(soup, known_teams):
    """Returns the season schedule that was able to be parsed"""
    parsed_matches = []
    rows = soup.select('table tr')
    # First 6 are headers
    for row in rows[6:-1]:
        parsed_matches.append(parse_row(row, known_teams))
    return parsed_matches
