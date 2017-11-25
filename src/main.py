import logging

import snc.scraper.scraper as bs_scraper

if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    bs_scraper.scrape_everything()
    # bs_scraper.test_api()

    # todo the client has to make server calls to decide whether to put or post. Server is basic right now and won't do those check