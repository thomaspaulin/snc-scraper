import json
import logging
import sys
from _datetime import datetime
from typing import Dict, List

import pytz
import requests
from bs4 import BeautifulSoup

import snc.scraper.printable_schedule as printable
import snc.scraper.teams as teams
from snc.scraper.constants import *
from snc.scraper.division import Division
from snc.scraper.league import League
from snc.scraper.match import Match, MatchType
from snc.scraper.match_summary import MatchSummary
from snc.scraper.rink import Rink
from snc.scraper.team import Team

l = logging.getLogger('scraper')


def get_known_teams() -> Dict[str, Team]:
    r = requests.get("{}/teams".format(API_URL))
    if r.status_code is not 200:
        return {}
    t = {}
    for json in r.json():
        team = Team.load(json)
        t[team.name.lower()] = team
    return t


def get_known_leagues() -> Dict[str, League]:
    r = requests.get("{}/leagues".format(API_URL))
    if r.status_code is not 200:
        return {}
    l = {}
    for json in r.json():
        league = League.load(json)
        l[league.name.lower()] = league
    return l


def get_known_divisions() -> Dict[str, Division]:
    r = requests.get("{}/divisions".format(API_URL))
    if r.status_code is not 200:
        return {}
    d = {}
    for json in r.json():
        div = Division.load(json)
        d[div.name.lower()] = div
    return d


def scrape_everything() -> None:
    l.setLevel(logging.DEBUG)
    l.info('=============================================================================')
    l.info('COMMENCING SCRAPING AT {} (UTC)'.format(datetime.utcnow()))
    l.info('=============================================================================')
    l.info('FETCHING KNOWN TEAMS AND DIVISIONS')
    l.info('=============================================================================')
    known_teams = get_known_teams()
    l.debug('Known teams:')
    l.debug(known_teams)
    known_divisions = get_known_divisions()
    l.debug('Known divisions')
    l.debug(known_divisions)
    l.info('=============================================================================')
    l.info('SAVING LEAGUES AND DIVISIONS')
    l.info('=============================================================================')
    l.debug('Warning: Not parsing leagues, instead using SNC, BHL, and FHL')
    league_snc = League(name='SNC')
    league_bhl = League(name='BHL')
    league_fhl = League(name='FHL')
    save_leagues([league_snc, league_bhl, league_fhl])
    known_leagues = get_known_leagues()

    l.debug('Warning: Not parsing divisions, instead using A, B, and C')
    div_a = Division(name="A")
    div_b = Division(name="B")
    div_c = Division(name="C")
    save_divisions([div_a, div_b, div_c])
    known_divisions = get_known_divisions()

    l.info('=============================================================================')
    l.info('SCRAPING START')
    l.info('=============================================================================')
    res = requests.get(SCHEDULES_URL)
    soup = BeautifulSoup(res.text, 'lxml')

    # The select options all take the format of 'YYYY SNC Season'
    season_str: str = '{}'.format(datetime.utcnow().year)
    # Name of the <select> element who sets the season,
    # also used for the POST
    selector_name: str = 'sel_ChildSeason'

    # These is only one thankfully but select returns a list, hence [0]
    select = soup.select('select[name={}]'.format(selector_name))[0]

    season_id: str = None

    for child in select.find_all('option'):
        if len(child.contents) is 1 and child.contents[0].startswith(season_str):
            season_id = child['value']

    # TODO EXPORT THE SEASON ID HERE FOR OTHERS TO KNOW ABOUT THEN IMPLEMENT THIS READING THE EXPORTED SEASONS (AS A CACHE)
    # Submit the season ID to get the one we are interested in
    # then start parsing
    l.info('Using season with ID: {}'.format(season_id))
    if season_id is not None:
        requests.post(SCHEDULES_URL,
                      data={selector_name.encode(), season_id.encode()})

    # TEAMS
    l.info('-----------------------------------------------------------------------------')
    l.info('BEGIN SCRAPING: Teams')
    l.info('-----------------------------------------------------------------------------')
    teams_res = requests.get(TEAMS_URL)
    parsed_teams: List[Team] = teams.parse(BeautifulSoup(teams_res.text, 'lxml'), known_teams, known_leagues,
                                           known_divisions)

    l.info('=============================================================================')
    l.info('SAVING TEAMS')
    l.info('=============================================================================')
    l.debug(parsed_teams)
    save_teams(parsed_teams)
    known_teams = get_known_teams()


    l.info('-----------------------------------------------------------------------------')
    l.info('BEGIN SCRAPING: Schedule')
    l.info('-----------------------------------------------------------------------------')
    # SCHEDULE
    printable_res = requests.get(PRINTABLE_SCHEDULE_URL)
    schedule = printable.parse(BeautifulSoup(printable_res.text, 'lxml'), known_teams)
    l.debug(schedule)
    l.info('=============================================================================')
    l.info('SAVING MATCHES')
    l.info('=============================================================================')
    save_matches(schedule)

    # l.info('-----------------------------------------------------------------------------')
    # l.info('BEGIN SCRAPING: Schedule URLs')
    # l.info('-----------------------------------------------------------------------------')
    # # BOXSCORES
    # schedule_page_urls = sched.get_schedule_urls(start_month=9, end_month=9)
    # match_summaries = []
    # for schedule_page_url in schedule_page_urls:
    #     schedule_page_res = requests.get(schedule_page_url)
    #     boxscore_urls = sched.parse_boxscore_urls(BeautifulSoup(schedule_page_res.text, 'lxml'), BASE_URL)
    #     for boxscore_url in boxscore_urls:
    #         boxscore_res = requests.get(boxscore_url)
    #         match_summaries.append(boxscore.parse_page(BeautifulSoup(boxscore_res.text, 'lxml'), known_teams))

    # l.info('=============================================================================')
    # l.info('SAVING SUMMARIES')
    # l.info('=============================================================================')
    # save_summaries(match_summaries)

    l.info('=============================================================================')
    l.info('FINISHED')
    l.info('=============================================================================')


def test_api(known_teams: Dict[str, Team], known_divisions: Dict[str, Division]) -> None:
    l.setLevel(logging.DEBUG)
    snc_divisions = [
        Division(name='Python C'),
        Division(name='Python B')
    ]
    # saveDivisions(snc_divisions)

    # todo create some teams, matches, match sumamries to test with
    snc_teams = [
        Team(name='Python Bears', division_name='Python C', logo_url='test'),
        Team(name='Python Grizzlies', division_name='Python B', logo_url='test2'),
        Team(name='Python Hawks', division_name='Python C', logo_url='test3')
    ]
    # saveTeams(snc_teams)

    matches = [
        Match(game_type=MatchType.PRACTICE,
              start=datetime(2017, 3, 24, 16, 30, 0, 0).replace(tzinfo=pytz.UTC),
              season=2017,
              away=snc_teams[0],
              home=snc_teams[1],
              rink=Rink(name='Python Avondale')),
        Match(game_type=MatchType.REGULAR_SEASON,
              season=2017,
              start=datetime(2017, 3, 25, 16, 30, 0, 0).replace(tzinfo=pytz.UTC),
              away=snc_teams[2],
              home=snc_teams[1],
              away_score=1,
              home_score=3,
              rink=Rink(name='Python Botany'))
    ]
    save_matches(matches)

    # TODO test with players and everything
    summaries = [
        MatchSummary(start=datetime.utcnow().replace(tzinfo=pytz.UTC),
                     rink=Rink(name='Python Avondale'),
                     away=snc_teams[2],
                     home=snc_teams[1],
                     away_score=1,
                     home_score=3)
    ]
    save_summaries(summaries)


def submit(a_url: str, a_list: List) -> None:
    """Submits to the server. The list items must know how to serialise themselves"""
    for i in a_list:
        try:
            payload = json.dumps(i.dump())
        except AttributeError:
            print('Submit called on a None type')
            payload = {}
        l.debug(payload)
        r = requests.post(a_url, data=payload)
        if r.status_code is not 200:
            l.fatal('Response status: {}'.format(r.status_code))
            l.fatal(r.json())
            l.fatal('Payload was:')
            l.fatal(payload)
            sys.exit()


def save_leagues(leagues: List[League] = None) -> None:
    leagues_url = '{}/leagues'.format(API_URL)
    submit(leagues_url, leagues)


def save_divisions(divisions: List[Division]=None) -> None:
    divisions_url = '{}/divisions'.format(API_URL)
    submit(divisions_url, divisions)


def save_teams(teams: List[Team]=None) -> None:
    teams_url = '{}/teams'.format(API_URL)
    submit(teams_url, teams)


def save_matches(schedule: List[Match]=None) -> None:
    matches_url = '{}/matches'.format(API_URL)
    submit(matches_url, schedule)
    # pass


def save_summaries(summaries: List[MatchSummary]=None) -> None:
    # not supported on server yet
    pass
