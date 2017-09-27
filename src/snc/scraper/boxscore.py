"""
For scraping
http://www.aucklandsnchockey.com/leagues/hockey_boxscores_printable.cfm?clientID=5788&leagueID=23341&gameID=[some-id-here]
That is, it is for scraping the match information
"""
import time
from players import Goalie, Player
from parsing_utils import capitalise
from match_summary import MatchSummary


def parse_teams(elem):
    """Returns the teams involved in the match"""
    cell = elem.select('tr')[1:2][0]
    away = cell.contents[1].select('font')[0].contents[0].contents[0].strip()
    home = cell.contents[4].select('font')[0].contents[0].contents[0].strip()
    return {'away': away, 'home': home}


def parse_goals(elem):
    """Returns all the goals scored indexed by team"""
    # 1. Parse the score up the top and use that as the authority
    # 2. Parse the scoring table
    # 3. Verify scoring table vs scores up top
    # 4. Parse the scoring summary
    # 5. Verify scoring summary vs. scoring table vs. top scores
    # 6. Submit everything but have a warning to display on the UI
    #    if the information didn't match up. If there is more in
    #    tables than up top, omit the tables
    # TODO
    pass


def parse_shots(elem):
    """Returns all the shots on goal per period indexed by team"""
    shots = {}
    rows = elem.select('tr')
    for row in rows[1:]:
        cells = row.select('td')
        team = cells[0].contents[0].strip()
        try:
            period_1 = int(cells[1].contents[0].strip())
        except ValueError:
            period_1 = 0
        try:
            period_2 = int(cells[2].contents[0].strip())
        except ValueError:
            period_2 = 0
        try:
            period_3 = int(cells[3].contents[0].strip())
        except ValueError:
            period_3 = 0
        # the total is in bold so need contents twice
        total = int(cells[4].contents[0].contents[0].strip())
        if (period_1 + period_2 + period_3) is not total:
            raise ValueError('Shots by period did not match the declared total')
        else:
            shots[team] = (period_1, period_2, period_3)
    return shots


def parse_power_plays(elem):
    """Returns the a tuple of the successful power plays and total power plays
    in a dictionary indexed by team
    """
    pps = {}
    rows = elem.select('tr')
    for row in rows[1:]:
        cells = row.select('td')
        team = cells[0].contents[0].strip()
        power_plays = cells[1].contents[0].strip().split(' for ')
        pps[team] = (int(power_plays[0]), int(power_plays[1]))
    return pps


def parse_details(elem):
    """Returns the match details in a dictionary"""
    details = {}
    rows = elem.select('tr')
    for row in rows[1:]:
        cells = row.select('td')
        key = capitalise(cells[0].contents[0].strip())
        value = cells[1].contents[0].strip()
        details[key] = value
    return details


def parse_penalties(elem):
    """Returns the penalties indexed by team"""
    # TODO
    pass


def correct_team_table(title_row, team):
    """Returns True if the table is for the specified team"""
    tbl_header = title_row.select('td')[0].contents[0]
    try:
        name = tbl_header.contents[0]
    except AttributeError:
        name = tbl_header
        pass
    name = name.lower().strip().split(' ')[0]
    return name == team.lower().strip()


def parse_players(elem, team_name):
    """Returns a list of players"""
    players = []
    rows = elem.select('tr')
    if not correct_team_table(rows[0], team_name):
        raise ValueError('The provided team did not match that found in the '
                         'table header ')
    else:
        for row in rows[2:]:
            cells = row.select('td')
            number = int(cells[0].contents[0].strip())
            name = cells[1].contents[0].strip()
            # TODO the rest of the information
            players.append(Player(
                number=number,
                name=name))
    return players


def parse_goalies(elem, team_name):
    """Returns a list of goalies"""
    goalies = []
    rows = elem.select('tr')
    if not correct_team_table(rows[0], team_name):
        raise ValueError('The provided team did not match that found in the '
                         'table header ')
    else:
        for row in rows[2:]:
            cells = row.select('td')
            number = int(cells[0].contents[0].strip())
            name = cells[1].contents[0].strip()
            mins_str = cells[2].contents[0].strip()
            mins = time.strptime(mins_str, '%M:%S')
            shots_faced = int(cells[3].contents[0].strip())
            saves_made = int(cells[4].contents[0].strip())
            goalies.append[Goalie(
                number=number,
                name=name)]
    return goalies


def parse_page(soup):
    """Returns a MatchSummary object that represents the given box score page"""
    tables = soup.select('table.boxscores')
    teams = parse_teams(tables[0])
    # TODO need to parse the start time and rink properly too
    # TODO reconsider this because on the example page some goals are missing from the who and when
    # tables[5] for goals who and When
    # tables[1] for goals by period and total
    # goals = parse_goals()
    shots_on_goal = parse_shots(tables[2])
    power_plays = parse_power_plays(tables[3])
    details = parse_details(tables[4])
    penalies = parse_penalties(tables[6])
    away_players = parse_players(tables[7], teams['away'])
    home_players = parse_players(tables[9], teams['home'])
    away_goalies = parse_goalies(tables[8], teams['away'])
    home_goalies = parse_goalies(tables[10], teams['home'])
    # TODO
    return MatchSummary()
