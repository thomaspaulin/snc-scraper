from datetime import datetime
from pytz import timezone, utc
from bs4 import BeautifulSoup


def parse_date(date_str):
    """Returns a date parsed from a date string in the format In the format SA 18-Mar-2017 4:30P. Dates parsed will be in UTC"""
    ds = date_str.strip() + 'M'
    tz = timezone("Pacific/Auckland")
    days = { 'SA': 'Saturday', 'SU': 'Sunday', 'MO': 'Monday' }
    for day in days:
        if day in ds:
            ds = ds.replace(day, days[day])
    date = tz.localize(datetime.strptime(ds, '%A %d-%b-%Y %I:%M%p'));
    return date.astimezone(utc)
