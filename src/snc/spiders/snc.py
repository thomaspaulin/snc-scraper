# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import scrapy


class SncSpider(scrapy.Spider):
    name = "snc"
    allowed_domains = ["www.aucklandsnchockey.com"]
    start_urls = ['http://www.aucklandsnchockey.com/leagues/teams.cfm?leagueID=23341&clientID=5788']

    def start_requests(self):
        for url in self.start_urls:
            return [scrapy.FormRequest(url, callback=self.set_season)]


    def set_season(self, response):
        """
        Set the season so we can start downloading pages to give to the scrapers
        """
        # The select options all take the format of 'YYYY SNC Season'
        season_str = '{} SNC Season'.format(datetime.utcnow().year)
        # Name of the <select> element who sets the season, also used for the POST
        selector_name = 'sel_ChildSeason'

        soup = BeautifulSoup(response.text, 'lxml')
        select = soup.select('select[name={}]'.format(selector_name))[0]
        for child in select.find_all('option'):
            if len(child.contents) is 1 and child.contents is season_str:
                season_id = child['value']
        if season_id is not None:
            # TODO EXPORT THE SEASON ID HERE FOR OTHERS TO KNOW ABOUT THEN IMPLEMENT THIS READING THE EXPORTED SEASONS (AS A CACHE)
            # Submit the season ID to get the one we are interested in then start parsing
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
        Request('http://www.aucklandsnchockey.com/leagues/print_schedule.cfm?leagueID=23341&clientID=5788&teamID=0&mixed=1',
                callback=parse_printable_schedule);

        Request('http://www.aucklandsnchockey.com/leagues/teams.cfm?leagueID=23341&clientID=5788',
                callback=parse_team_page);

    def parse_printable_schedule(self, response):
        parser = new PrintableScheduleParser(BeautifulSoup(response.text, 'lxml'))
        schedule = parser.parse();
        # TODO write the utils to some form of data storage

    def parse_team_page(self, respoonse):
        parser = new TeamParser(BeautifulSoup(response.text, 'lxml'))
        teams = parser.parse()
        # TODO write the utils to some form of data storage
