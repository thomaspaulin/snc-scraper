from datetime import datetime

"""
For parsing
http://www.aucklandsnchockey.com/leagues/schedules.cfm?clientid=5788&leagueid=23341
This page is used in addition to the printable schedule because the printable
schedule does not have the boxscore links but for everything else the printable
schedule is preferred because it has the whole season on one page so fewer
requests are made
"""


# TODO ADD selectedMonth=3&selectedYear=2017 to get the month of interest page


def parse_boxscore_urls(soup, base_url):
    """Returns the boxscore URLs for all those matches with them

    Note: To use a selectedYear that is not the current season's year you must
          change season otherwise no games will be shown

          e.g.,
          You cannot be in the 2017 season and use selectedYear=2016
    """
    try:
        links = soup.select('table.boxscores')[4].select('a')
    except IndexError:
        return []
    boxscore_anchor_elems = [
        x for x in links if 'hockey_boxscores' in x['href']
    ]
    return [
        (base_url + elem['href']).replace('hockey_boxscores.cfm', 'hockey_boxscores_printable.cfm')
        for elem in boxscore_anchor_elems
    ]


def get_schedule_urls(year=datetime.utcnow().year, start_month=1, end_month=12):
    """
    Returns the URLs of each schedule page up to the given date's month

    NB: Day is not supported by the website, only month and year
    """
    template = 'http://www.aucklandsnchockey.com/leagues/schedules.cfm' \
               '?selectedMonth={}' \
               '&selectedYear={}' \
               '&leagueID=23341' \
               '&clientID=5788'
    if start_month > end_month:
        raise ValueError('start_month must be less than or equal to end_month')
    urls = []
    for month in range(start_month, end_month + 1):
        urls.append(template.format(month, year))
    return urls
