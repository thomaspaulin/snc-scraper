# snc-scraper
[![Build Status](https://travis-ci.org/thomaspaulin/snc-scraper.svg?branch=master)](https://travis-ci.org/thomaspaulin/snc-scraper)

Scraping the Auckland SNC Hockey website one symbol at a time. (http://www.aucklandsnchockey.com)

## Foreword
At the time of writing this all the scraping is done in Beautiful Soup 4. There are plans to move it to use Scrapy
later down the lines.

## Setup
This repository uses Scrapy and Python3. To get set up do the following:

1. Install python3
2. Set up a virtual environment `virtualenv venv` or `virtualenv -p python3 venv`
3. Activate your virtual environment with `source venv/bin/activate`
4. `cd` into this repo
5. Run `pip install -r requirements.txt`
6. Write awesome code

## Running
`python src/main.py` (builds not yet implemented)

## Scraping in the REPL
`from bs4 import BeautifulSoup`

`import requests`

`r = requests.get([url goes here])`

`soup = BeautifulSoup(r.text, 'lxml')`
