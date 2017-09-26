import bs4
from bs4 import BeautifulSoup
import schedule_util
from match import Match

def parse_score(score_elem):
    """Returns the score parsed from the provided bs4 Tag or -1 if there wasn't one"""
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

def parse_team(team_elem):
    """Returns the team name parsed from the provided bs4 Tag"""
    if isinstance(team_elem, bs4.element.Tag):
        team_elem = team_elem.contents[0]
    try:
        return team_elem.strip()
    except TypeError:
        return team_elem.select('b')[0].contents[0].strip()

def parse_rink(rink_elem):
    if isinstance(rink_elem, bs4.element.Tag):
        rink_elem = rink_elem.contents[0]
    return rink_elem.strip()[:-5]

def parse_row(row_elem):
    tds = row_elem.select('td');

    # Playoff rows have these header ones before them to indicate which game they are
    is_match_row = len(tds[0].select('img')) is 0
    if is_match_row:
        game_type_acronym = tds[0].select('font')[0].contents[0].strip()

        # In the format SA 18-Mar-2017 4:30P
        date = schedule_util.parse_date(tds[1].contents[0].strip() + ' ' + tds[2].contents[0].strip())
        # practice and regular season
        away = parse_team(tds[3].contents[0])
        away_score = parse_score(tds[4].contents[0])
        home = parse_team(tds[5].contents[0])
        home_score = parse_score(tds[6].contents[0])
        rink = parse_rink(tds[7].contents[0])

        return Match(gametype=game_type_acronym,
                     season=date.year,
                     start=date,
                     away=away,
                     home=home,
                     awayscore=away_score,
                     homescore=home_score,
                     rink=rink);
    else:
        return None

# For parsing http://www.aucklandsnchockey.com/leagues/print_schedule.cfm?leagueID=23341&clientID=5788&teamID=0&mixed=1
class PrintableScheduleParser:
    def __init__(self, schedule_page_soup):
        self.soup = schedule_page_soup

    def parse(self):
        """Returns the season schedule that was able to be parsed"""
        parsed_matches = [];
        rows = self.soup.select('table tr')
        # First 6 are headers
        for row in rows[6:-1]:
            parsed_matches.append(parse_row(row))
        return parsed_matches;
