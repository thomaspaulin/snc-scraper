from _datetime import datetime

import json
import logging
import pytz
import requests
from bs4 import BeautifulSoup

import snc.scraper.boxscore as boxscore
import snc.scraper.printable_schedule as printable
import snc.scraper.schedule as sched
import snc.scraper.teams as teams
from snc.scraper.division import Division
from snc.scraper.match import Match, MatchType
from snc.scraper.match_summary import MatchSummary
from snc.scraper.rink import Rink
from snc.scraper.team import Team

base_url = 'http://www.aucklandsnchockey.com/leagues/'
api_url = 'https://snc-api.herokuapp.com/api/v0'

l = logging.getLogger('scraper')


def scrape_everything():
    l.setLevel(logging.DEBUG)
    print('=============================================================================')
    print('SCRAPING START')
    print('=============================================================================')
    res = requests.get('http://www.aucklandsnchockey.com/leagues/schedules.cfm?clientid=5788&leagueid=23341')
    soup = BeautifulSoup(res.text, 'lxml')

    # The select options all take the format of 'YYYY SNC Season'
    season_str = '{} SNC Season'.format(datetime.utcnow().year)
    # Name of the <select> element who sets the season,
    # also used for the POST
    selector_name = 'sel_ChildSeason'

    # These is only one thankfull but select returns a list, hence [0]
    select = soup.select('select[name={}]'.format(selector_name))[0]

    season_id = None

    for child in select.find_all('option'):
        if len(child.contents) is 1 and child.contents is season_str:
            season_id = child['value']

    # TODO EXPORT THE SEASON ID HERE FOR OTHERS TO KNOW ABOUT THEN IMPLEMENT THIS READING THE EXPORTED SEASONS (AS A CACHE)
    # Submit the season ID to get the one we are interested in
    # then start parsing
    print('Using season with ID: {}'.format(season_id))
    if season_id is not None:
        requests.post('http://www.aucklandsnchockey.com/leagues/schedules.cfm?clientid=5788&leagueid=23341',
                      data={selector_name, season_id})

    # TEAMS
    print('-----------------------------------------------------------------------------')
    print('BEGIN SCRAPING: Teams')
    print('-----------------------------------------------------------------------------')
    teams_res = requests.get('http://www.aucklandsnchockey.com/leagues/teams.cfm?leagueID=23341&clientID=5788')
    parsed_teams = teams.parse(BeautifulSoup(teams_res.text, 'lxml'))
    print(parsed_teams)

    print('-----------------------------------------------------------------------------')
    print('BEGIN SCRAPING: Schedule')
    print('-----------------------------------------------------------------------------')
    # SCHEDULE
    printable_res = requests.get('http://www.aucklandsnchockey.com/leagues/print_schedule.cfm?leagueID=23341&clientID=5788&teamID=0&mixed=1')
    schedule = printable.parse(BeautifulSoup(printable_res.text, 'lxml'))
    print(schedule)

    print('-----------------------------------------------------------------------------')
    print('BEGIN SCRAPING: Schedule URLs')
    print('-----------------------------------------------------------------------------')
    # BOXSCORES
    schedule_page_urls = sched.get_schedule_urls(start_month=9, end_month=9)
    match_summaries = []
    for schedule_page_url in schedule_page_urls:
        schedule_page_res = requests.get(schedule_page_url)
        boxscore_urls = sched.parse_boxscore_urls(BeautifulSoup(schedule_page_res.text, 'lxml'), base_url)
        for boxscore_url in boxscore_urls:
            boxscore_res = requests.get(boxscore_url)
            match_summaries.append(boxscore.parse_page(BeautifulSoup(boxscore_res.text, 'lxml')))

    print('=============================================================================')
    print('SCRAPING FINISHED')
    print('=============================================================================')

    print('=============================================================================')
    print('STARTING API REQUESTS')
    print('=============================================================================')
    save_teams(parsed_teams)
    save_matches(schedule)
    save_summaries(match_summaries)


def test_api():
    l.setLevel(logging.DEBUG)
    snc_divisions = [
        Division(name='Python C'),
        Division(name='Python B')
    ]
    # saveDivisions(snc_divisions)

    # todo create some teams, matches, match sumamries to test with
    snc_teams = [
        Team(name='Python Bears', division=Division(name='Python C'), logo_url='test'),
        Team(name='Python Grizzlies', division=Division(name='Python B'), logo_url='test2'),
        Team(name='Python Hawks', division=Division(name='Python C'), logo_url='test3')
    ]
    # saveTeams(snc_teams)

    matches = [
        Match(game_type=MatchType.PRACTICE,
              start=datetime.now().replace(tzinfo=pytz.UTC),
              season=2017,
              away=snc_teams[0],
              home=snc_teams[1],
              rink=Rink(name='Python Avondale')),
        Match(game_type=MatchType.REGULAR_SEASON,
              season=2017,
              start=datetime.now().replace(tzinfo=pytz.UTC),
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


def submit(a_url, a_list):
    """Submits to the server. The list items must know how to serialise themselves"""
    for i in a_list:
        try:
            payload = json.dumps(i.dump())
        except AttributeError:
            print('Submit called on a None type')
            payload = {}
        l.debug(payload)
        requests.post(a_url, data=payload)


def save_divisions(divisions=None):
    pass
#     divisions_url = '{}/divisions'.format(api_url)
#     submit(divisions_url, divisions)


def save_teams(teams=None):
    pass
#     teams_url = '{}/teams'.format(api_url)
#     submit(teams_url, teams)


def save_matches(schedule=None):
    matches_url = '{}/matches'.format(api_url)
    submit(matches_url, schedule)
    # pass


def save_summaries(summaries=None):
    # not supported on server yet
    pass
