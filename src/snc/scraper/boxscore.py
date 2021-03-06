"""
For scraping
http://www.aucklandsnchockey.com/leagues/hockey_boxscores_printable.cfm?clientID=5788&leagueID=23341&gameID=[some-id-here]
That is, it is for scraping the match information
"""
import time

from functools import reduce
from typing import Dict, List, Tuple

import datetime

from snc.scraper.goal import Goal, GoalType
from snc.scraper.match_summary import MatchSummary
from snc.scraper.parsing_utils import capitalise, parse_date, parse_int
from snc.scraper.penalty import Penalty
from snc.scraper.players import Goalie, Player
from snc.scraper.teams import Team
from snc.scraper.division import Division
from snc.scraper.rink import Rink


################################################################################
# TODO CLEAN UP THIS CODE
################################################################################


def parse_teams(elem, known_teams: Dict[str, Team]) -> Dict[str, Team]:
    """Returns the teams involved in the match"""
    cell = elem.select('tr')[1:2][0]
    away_name: str = cell.contents[1].select('font')[0].contents[0].contents[0].strip()
    try:
        away: Team = known_teams[away_name.lower()]
    except KeyError:
        away: Team = Team(name=capitalise(away_name), division_name='Unknown')
    home_name: str = cell.contents[4].select('font')[0].contents[0].contents[0].strip()
    try:
        home: Team = known_teams[home_name.lower()]
    except KeyError:
        home: Team = Team(name=capitalise(home_name), division_name='Unknown')
    return {'away': away, 'home': home}


def parse_by_period(table_rows) -> Dict[str, Dict]:
    """Returns the X per period e.g., shots or goals"""
    header_cells = table_rows[0].select('td')

    labels = {}
    for (idx, cell) in enumerate(header_cells[1:]):
        labels[idx] = cell.contents[0].strip().lower()
    by_team_by_period: Dict[str, Dict] = {}
    for row in table_rows[1:]:
        cells = row.select('td')
        team: str = cells[0].contents[0].lower().strip()
        try:
            # the total is in bold so need contents twice
            expected_total: int = parse_int(
                            cells[len(cells)-1].contents[0].contents[0],
                            0)
        except AttributeError:
            # in case the total isn't actually in bold, although I've never
            # seen this case
            expected_total: int = parse_int(
                            cells[len(cells)-1].contents[0],
                            0)

        by_period: Dict = {}
        for (idx, cell) in enumerate(cells[1:-1]):
            val: int = parse_int(cell.contents[0], 0)
            by_period[labels[idx]] = val

        actual_total: int = 0
        for (period, amt) in by_period.items():
            actual_total += amt

        if actual_total != expected_total:
            raise ValueError('Shots by period did not match the declared total'
                             '({} vs. {})'.format(expected_total, actual_total))
        else:
            by_team_by_period[team] = by_period
    return by_team_by_period


def parse_goals(scoring_summary_elem) -> Dict[str, Goal]:
    rows = scoring_summary_elem.select('tr')
    current_period = 1
    goals: Dict[str, Goal] = {}
    for row in rows[1:]:
        cells = row.select('td')
        try:
            # Header row
            row_contents = cells[0].contents[0].contents[0].strip()
            goal_details = ''
        except AttributeError:
            # Penalty rows have a \n at the 0th index
            row_contents = ''
            goal_details = (cells[0].contents[1].contents[0].strip()
                            + ' ' + cells[0].contents[2].strip())
        if 'PERIOD' in row_contents:
            # This row is a a period header
            # e.g., PERIOD 1
            current_period: int = parse_int(row_contents.split(' ')[1], 1)
        else:
            # Looks like
            # Spartans at 10:42 - Joseph Hyun (unassisted)
            # Spartans at 6:48 - Wesley Bindell from Jordan Hills and Mike Davys
            # Spartans at 0:36 (PP) - Mike Davys from Joseph Hyun
            split = goal_details.split(' - ')
            team_time = split[0].split(' at ')
            if team_time[0].strip() == 'No Scoring':
                continue
            team: str = team_time[0].lower().strip()
            if '(' in team_time[1]:
                # Haven't seen what a short handed goal looks like yet
                idx = team_time[1].index('(')
                gt = team_time[1][idx+1: idx+2]
                if gt == 'PP':
                    goal_type = GoalType.POWER_PLAY
                elif gt == 'SH':
                    goal_type = GoalType.SHORTHANDED
                else:
                    goal_type = GoalType.REGULAR
                team_time[1] = team_time[1][0:idx]
            else:
                goal_type = GoalType.REGULAR
            time_str: str = team_time[1].strip()
            scorer_assists = split[1].split('from')
            try:
                scorer = scorer_assists[0].strip()
                assists: List[str] = scorer_assists[1].split(' and ')
                assists: List[str] = [x.strip() for x in assists]
            except IndexError:
                scorer: str = scorer_assists[0].strip()
                scorer: str = scorer[0:scorer.index('(unassisted)')].strip()
                assists: List[str] = []
            try:
                gs: List[Goal] = goals[team]
            except KeyError:
                gs: List[Goal] = []
            gs.append(Goal(goal_type=goal_type,
                           team=team,
                           period=current_period,
                           goal_time=time_str,
                           scorer=scorer,
                           assisted_by=assists))
            goals[team] = gs
    return goals


def parse_scores(by_period_elem, away: Team, home: Team) -> Dict[str, int]:
    """Returns all the goals scored indexed by team"""
    # 1. Parse the score up the top and use that as the authority
    # 2. Parse the scoring table
    # 3. Verify scoring table vs scores up top
    # 4. Parse the scoring summary
    # 5. Verify scoring summary vs. scoring table vs. top scores
    # 6. Submit everything but have a warning to display on the UI
    #    if the information didn't match up. If there is more in
    #    tables than up top, omit the tables
    by_period = parse_by_period(by_period_elem.select('tr'))
    away_count = reduce((lambda x, y: x + y), by_period[away.name.lower()].values())
    home_count = reduce((lambda x, y: x + y), by_period[home.name.lower()].values())
    return {away.name.lower(): away_count, home.name.lower(): home_count}


def parse_shots(elem):
    """Returns all the shots on goal per period indexed by team"""
    return parse_by_period(elem.select('tr'))


def parse_power_plays(elem) -> Dict[str, Tuple[int, int]]:
    """Returns the a tuple of the successful power plays and total power plays
    in a dictionary indexed by team
    """
    pps = {}
    rows = elem.select('tr')
    for row in rows[1:]:
        cells = row.select('td')
        team: str = cells[0].contents[0].strip()
        power_plays: List[str] = cells[1].contents[0].strip().split(' for ')
        pps[team]: Tuple[int, int] = (int(power_plays[0]), int(power_plays[1]))
    return pps


def parse_details(elem) -> Dict[str, str]:
    """Returns the match details in a dictionary"""
    details: Dict[str, str] = {}
    rows = elem.select('tr')
    for row in rows[1:]:
        cells = row.select('td')
        key: str = capitalise(cells[0].contents[0].strip())
        value: str = cells[1].contents[0].strip()
        details[key] = value
    return details


def parse_start(date_str: str, time_str: str) -> datetime:
    """Returns the match start datetime in UTC"""
    # Sep. 30, 2017 4:45PM
    s = date_str + ' ' + time_str
    return parse_date(s, '%b. %d, %Y %I:%M%p')


def parse_rink(rink_str: str) -> Rink:
    """Returns the rink the match was played at"""
    return Rink(name=rink_str.split(' ')[0].strip())


def parse_penalties(elem) -> Dict[str, Penalty]:
    """Returns the penalties indexed by team"""
    rows = elem.select('tr')
    current_period: int = 1
    penalties: Dict[str, Penalty] = {}
    for row in rows[1:]:
        cells = row.select('td')
        try:
            # Header row
            row_contents: str = cells[0].contents[0].contents[0].strip()
            penalty_details: str = ''
        except AttributeError:
            # Penalty rows have a \n at the 0th index
            row_contents: str = ''
            penalty_details: str = (cells[0].contents[1].contents[0].strip()
                               + ' ' + cells[0].contents[2].strip())
        if 'PERIOD' in row_contents:
            # This row is a a period header
            # e.g., PERIOD 1
            current_period: int = parse_int(row_contents.split(' ')[1], 1)
        else:
            # Looks like
            # Shannon at 3:23 - Sean Brantsma for Unsportsmanlike Conduct (2 Min.)
            p: List[str] = penalty_details.split(' - ')
            team_time: List[str] = p[0].split(' at ')
            if team_time[0].strip() == 'No Penalties':
                continue
            team: str = team_time[0]
            time_str: str = team_time[1]
            o: List[str] = p[1].split(' for ')
            offender: str = o[0]
            # Penalties can be two words. Only the ( is constant
            penalty_and_pim: List[str] = o[1].split('(')
            offense: str = penalty_and_pim[0].strip()
            # Trim off "Min.)"
            pim: int = parse_int(penalty_and_pim[1].strip()[:-5].strip(), 0)
            try:
                ps: List[Penalty] = penalties[team.lower()]
            except KeyError:
                ps: List[Penalty] = []
            ps.append(Penalty(offense=offense,
                              period=current_period,
                              penalty_time=int(time_str),
                              team=team,
                              offender=offender,
                              pim=pim))
            penalties[team.lower()] = ps
    return penalties


def parse_players(elem) -> List[Player]:
    """Returns a list of players"""
    players: List[Player] = []
    rows = elem.select('tr')
    for row in rows[2:]:
        try:
            cells = row.select('td')
            number: int = int(cells[0].contents[0].strip())
            name: str = cells[1].contents[0].strip()
            players.append(Player(
                number=number,
                name=name))
        except ValueError:
            continue
    return players


def parse_goalies(elem) -> List[Goalie]:
    """Returns a list of goalies"""
    goalies: List[Goalie] = []
    rows = elem.select('tr')
    for row in rows[2:]:
        try:
            cells = row.select('td')
            number: int = int(cells[0].contents[0].strip())
            name: str = cells[1].contents[0].strip()
            mins_str: str = cells[2].contents[0].strip()
            mins: int = time.strptime(mins_str, '%M:%S')
            shots_faced: int = int(cells[3].contents[0].strip())
            saves_made: int = int(cells[4].contents[0].strip())
            # Note: These are all on a per game basis and should be combined with the season wide stats in the database
            goalies.append(Goalie(
                number=number,
                name=name,
                mins=mins,
                shots_faced=shots_faced,
                saves_made=saves_made))
        except ValueError:
            continue
    return goalies


def parse_page(soup, known_teams: Dict[str, Team]) -> MatchSummary:
    """Returns a MatchSummary object that represents the given box score page"""
    tables = soup.select('table.boxscores')
    try:
        teams: Dict[str, Team] = parse_teams(tables[0], known_teams)
        away: Team = teams['away']
        home: Team = teams['home']
    except IndexError:
        print(soup)
        raise IndexError('halp')

    # tables[5] for scoring summary
    # tables[1] for goals by period and total
    score = parse_scores(tables[1], away, home)
    goals = parse_goals(tables[5])
    shots_on_goal = parse_shots(tables[2])
    power_plays = parse_power_plays(tables[3])
    details = parse_details(tables[4])

    start: datetime = parse_start(details['Game Date'], details['Start Time'])
    rink: Rink = parse_rink(details['Location'])
    penalties: Dict[str, Penalty] = parse_penalties(tables[6])

    players = {
        away: parse_players(tables[7]),
        home: parse_players(tables[9])
    }
    goalies = {
        away: parse_goalies(tables[8]),
        home: parse_goalies(tables[10])
    }
    return MatchSummary(start=start,
                        rink=rink,
                        away=away,
                        home=home,
                        away_score=score[away.name.lower()],
                        home_score=score[home.name.lower()],
                        goals=goals,
                        shots=shots_on_goal,
                        power_plays=power_plays,
                        penalties=penalties,
                        players=players,
                        goalies=goalies)
