"""
For scraping
http://www.aucklandsnchockey.com/leagues/hockey_boxscores_printable.cfm?clientID=5788&leagueID=23341&gameID=[some-id-here]
That is, it is for scraping the match information
"""
import time
from players import Goalie, Player
from parsing_utils import capitalise, parse_date, parse_int
from match_summary import MatchSummary
from penalty import Penalty


def parse_teams(elem):
    """Returns the teams involved in the match"""
    cell = elem.select('tr')[1:2][0]
    away = capitalise(cell
                      .contents[1]
                      .select('font')[0]
                      .contents[0]
                      .contents[0]
                      .strip())
    home = capitalise(cell
                      .contents[4]
                      .select('font')[0]
                      .contents[0]
                      .contents[0]
                      .strip())
    return {'away': away, 'home': home}


def parse_by_period(table_rows):
    """Returns the X per period e.g., shots or goals"""
    header_cells = table_rows[0].select('td')

    labels = {}
    for (idx, cell) in enumerate(header_cells[1:]):
        labels[idx] = cell.contents[0].strip().lower()
    by_team_by_period = {}
    for row in table_rows[1:]:
        cells = row.select('td')
        team = cells[0].contents[0].lower().strip()
        try:
            # the total is in bold so need contents twice
            expected_total = parse_int(
                            cells[len(cells)-1].contents[0].contents[0],
                            0)
        except AttributeError:
            # in case the total isn't actually in bold, although I've never
            # seen this case
            expected_total = parse_int(
                            cells[len(cells)-1].contents[0],
                            0)

        by_period = {}
        for (idx, cell) in enumerate(cells[1:-1]):
            val = parse_int(cell.contents[0], 0)
            by_period[labels[idx]] = val

        actual_total = 0
        for (period, amt) in by_period.items():
            actual_total += amt

        if actual_total != expected_total:
            raise ValueError('Shots by period did not match the declared total'
                             '({} vs. {})'.format(expected_total, actual_total))
        else:
            print('by period:')
            print(by_period)
            by_team_by_period[team] = by_period
    return by_team_by_period


def parse_goals(by_period_elem, scoring_summary_elem, away, home):
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
    by_period = parse_by_period(by_period_elem.select('tr'))
    away_by_period = by_period[away.lower()]
    home_by_period = by_period[home.lower()]
    # TODO parse the scoring summary and make the return type a list of goals by team
    return by_period


def parse_shots(elem):
    """Returns all the shots on goal per period indexed by team"""
    return parse_by_period(elem.select('tr'))


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


def parse_start(date_str, time_str):
    """Returns the match start datetime in UTC"""
    # Sep. 30, 2017 4:45PM
    s = date_str + ' ' + time_str
    return parse_date(s, '%b. %d, %Y %I:%M%p')


def parse_rink(rink_str):
    """Returns the rink the match was played at"""
    return rink_str.split(' ')[0].strip()


def parse_penalties(elem):
    """Returns the penalties indexed by team"""
    # TODO
    rows = elem.select('tr')
    current_period = 1
    penalties = {}
    for row in rows[1:]:
        cells = row.select('td')
        try:
            # Header row
            row_contents = cells[0].contents[0].contents[0].strip()
        except AttributeError:
            # Penalty rows have a \n at the 0th index
            row_contents = ''
            penalty_details = (cells[0].contents[1].contents[0].strip()
                               + ' ' + cells[0].contents[2].strip())
        if 'PERIOD' in row_contents:
            # This row is a a period header
            # e.g., PERIOD 1
            current_period = parse_int(row_contents.split(' ')[1], 1)
        elif 'No Penalties' in row_contents:
            continue
        else:
            # Looks like
            # Shannon at 3:23 - Sean Brantsma for Unsportsmanlike Conduct (2 Min.)
            p = penalty_details.split(' - ')
            team_and_time = p[0].split(' at ')
            team = team_and_time[0]
            time_str = team_and_time[1]
            o = p[1].split(' for ')
            offender = o[0]
            # Penalties can be two words. Only the ( is constant
            penalty_and_pim = o[1].split('(')
            offense = penalty_and_pim[0].strip()
            # Trim off "Min.)"
            pim = parse_int(penalty_and_pim[1].strip()[:-5].strip(), 0)
            try:
                ps = penalties[team.lower()]
            except KeyError:
                ps = []
            ps.append(Penalty(offense=offense,
                              period=current_period,
                              penalty_time=time_str,
                              team=team,
                              offender=offender,
                              pim=pim))
            penalties[team.lower()] = ps
    return penalties


def correct_team_table(title_row, team):
    """Returns True if the table is for the specified team"""
    tbl_header = title_row.select('td')[0].contents[0]
    try:
        name = tbl_header.contents[0]
    except AttributeError:
        name = tbl_header
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
                name=name,
                position='?'))
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
            goalies.append(Goalie(
                number=number,
                name=name))
    return goalies


def parse_page(soup):
    """Returns a MatchSummary object that represents the given box score page"""
    tables = soup.select('table.boxscores')
    teams = parse_teams(tables[0])
    away = teams['away']
    home = teams['home']
    # tables[5] for scoring summary
    # tables[1] for goals by period and total
    goals = parse_goals(tables[1], tables[5], away, home)
    shots_on_goal = parse_shots(tables[2])
    power_plays = parse_power_plays(tables[3])
    details = parse_details(tables[4])
    start = parse_start(details['Game Date'], details['Start Time'])
    rink = parse_rink(details['Location'])
    penalies = parse_penalties(tables[6])

    players = {}
    players[away] = parse_players(tables[7], away)
    players[home] = parse_players(tables[9], home)
    goalies = {}
    goalies[away] = parse_goalies(tables[8], away)
    goalies[home] = parse_goalies(tables[10], home)
    return MatchSummary(start=start,
                        rink=rink,
                        away=away,
                        home=home,
                        away_score=None,    # TODO
                        home_score=None,    # TODO
                        goals=goals,
                        shots=shots_on_goal,
                        power_plays=power_plays,
                        penalties=penalies,
                        players=players,
                        goalies=goalies)
