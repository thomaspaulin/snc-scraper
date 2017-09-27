from bs4 import BeautifulSoup

# For parsing http://www.aucklandsnchockey.com/leagues/schedules.cfm?clientid=5788&leagueid=23341
# This page is used in addition to the printable schedule because the printable schedule does not
#   have the boxscore links but for everything else the printable schedule is preferred because
#   it has the whole season on one page so fewer requests are made

#TODO ADD selectedMonth=3&selectedYear=2017 to get the month of interest page

def parse_boxscore_urls(soup):
    """Returns the boxscore URLs for all those matches with them

    Note: To use a selectedYear that is not the current season's year you must
          change season otherwise no games will be shown

          e.g.,
          You cannot be in the 2017 season and use selectedYear=2016
    """
    links = soup.select('table.boxscores')[4].select('a')
    boxscore_anchor_elems = [x for x in links if 'hockey_boxscores' in x['href']]
    return [elem['href'] for elem in boxscore_anchor_elems]
