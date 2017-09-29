# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import scrapy
import snc.scraper.schedule
import snc.scraper.boxscore
import snc.scraper.teams
import snc.scraper.printable_schedule


################################################
# TODO
# 0. Use BeautifulSoup only to get the sites and parse.
#
# 1. Have Scrapy download the schedule and team pages
# 2. Have Scrapy parse the boxscore URLs then crawl the response
# 3. Call scripts that run the created parsers outside of Scrapy, at a different
#   pipeline step
################################################

class SncSpider(scrapy.Spider):
    name = "snc"
    allowed_domains = ["www.aucklandsnchockey.com"]
    start_urls = [
        'http://www.aucklandsnchockey.com/leagues/teams.cfm?leagueID=23341&clientID=5788'
    ]

    base_url = 'http://www.aucklandsnchockey.com/leagues/'

    def start_requests(self):
        for url in self.start_urls:
            return [scrapy.FormRequest(url, callback=self.set_season)]

    def set_season(self, response):
        """
        Set the season so we can start downloading pages to give to the scrapers
        """
        # The select options all take the format of 'YYYY SNC Season'
        season_str = '{} SNC Season'.format(datetime.utcnow().year)
        # Name of the <select> element who sets the season,
        # also used for the POST
        selector_name = 'sel_ChildSeason'

        soup = BeautifulSoup(response.text, 'lxml')
        select = soup.select('select[name={}]'.format(selector_name))[0]
        for child in select.find_all('option'):
            if len(child.contents) is 1 and child.contents is season_str:
                season_id = child['value']
        if season_id is not None:
            # TODO EXPORT THE SEASON ID HERE FOR OTHERS TO KNOW ABOUT THEN IMPLEMENT THIS READING THE EXPORTED SEASONS (AS A CACHE)
            # Submit the season ID to get the one we are interested in
            # then start parsing
            yield FormRequest(response.url,
                              formdata={selector_name: season_id},
                              callback=self.parse)
        else:
            # Assume the current year if a season ID can't be found
            # Then start parsing
            yield Request(response.url, callback=self.parse)

    def parse(self, response):
        """Parses the various page. Does not return anything"""
        # TODO is yield necessary?

        # Parse the schedule
        Request('http://www.aucklandsnchockey.com/leagues/print_schedule.cfm?leagueID=23341&clientID=5788&teamID=0&mixed=1',
                callback=parse_printable_schedule)

        # Parse the teams page
        Request('http://www.aucklandsnchockey.com/leagues/teams.cfm?leagueID=23341&clientID=5788',
                callback=parse_team_page)

        # Parse the box score URLs
        Request('http://www.aucklandsnchockey.com/leagues/schedules.cfm?clientid=5788&leagueid=23341',
                callback=parse_boxscore_urls)

    def parse_printable_schedule(self, response):
        schedule = printable_schedule.parse(
                    BeautifulSoup(response.text, 'lxml'))
        # TODO write the utils to some form of data storage

    def parse_team_page(self, respoonse):
        teams = teams.parse(BeautifulSoup(response.text, 'lxml'))
        # TODO write the utils to some form of data storage

    def parse_boxscores(self, response):
        boxscore.parse_page(BeautifulSoup(response.text, 'lxml'))
        # TODO write out

    def parse_boxscore_urls(self, response):
        urls = snc.scraper.schedule.parse_boxscore_urls(
            BeautifulSoup(response.text, 'lxml'),
            self.base_url)

        for url in urls:
            yield Request(url, callback=boxscore.parse_boxscores)
