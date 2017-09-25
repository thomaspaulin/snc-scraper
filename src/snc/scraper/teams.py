from bs4 import BeautifulSoup

# For parsing http://www.aucklandsnchockey.com/leagues/teams.cfm?leagueID=23341&clientID=5788
class TeamParser:
    soup

    def __init__(self, team_page_soup):
        self.soup = team_page_soup

    def parse(self):
        """Returns the teams in the league that could be parsed"""
        pass
