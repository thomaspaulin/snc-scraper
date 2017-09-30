from _datetime import datetime

import requests
from bs4 import BeautifulSoup

import snc.scraper.boxscore as boxscore
import snc.scraper.printable_schedule as printable
import snc.scraper.schedule as sched
import snc.scraper.teams as teams

base_url = 'http://www.aucklandsnchockey.com/leagues/'


def scrape_everything():
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
    #print(match_summaries)

