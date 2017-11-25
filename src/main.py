import logging
import requests

import snc.scraper.scraper as bs_scraper
from snc.scraper.constants import *
from snc.scraper.teams import Team
from snc.scraper.division import Division
from typing import Dict


def get_known_teams() -> Dict[str, Team]:
    r = requests.get("{}/teams".format(API_URL))
    if r.status_code is not 200:
        return {}
    t = {}
    for json in r.json():
        team = Team.load(json)
        t[team.name.lower()] = team
    return t


def get_known_divisions() -> Dict[str, Division]:
    r = requests.get("{}/divisions".format(API_URL))
    if r.status_code is not 200:
        return {}
    d = {}
    for json in r.json():
        div = Division.load(json)
        d[div.name.lower()] = div
    return d


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    teams = get_known_teams()
    divisions = get_known_divisions()

    bs_scraper.scrape_everything(teams, divisions)
    # bs_scraper.test_api(teams, divisions)

    # todo the client has to make server calls to decide whether to put or post. Server is basic right now and won't do those check