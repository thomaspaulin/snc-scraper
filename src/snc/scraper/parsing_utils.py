from datetime import datetime, timedelta
from pytz import timezone, utc


def capitalise(string) -> str:
    words = string.strip().lower().split(' ')
    upper_words = []
    for word in words:
        upper_words.append(word[0:1].upper() + word[1:])
    return ' '.join(upper_words)


def parse_date(date_str, str_format) -> datetime:
    tz = timezone("Pacific/Auckland")
    return tz.localize(datetime.strptime(date_str, str_format))


def parse_int(int_str, default) -> int:
    try:
        return int(int_str)
    except ValueError:
        return default


def parse_schedule_date(date_str) -> datetime:
    """Returns a date parsed from a date string in the format In the format
    SA 18-Mar-2017 4:30P. Dates parsed will be in UTC"""
    ds = date_str.strip() + 'M'
    tz = timezone("Pacific/Auckland")
    days = {
        'SA': 'Saturday',
        'SU': 'Sunday',
        'MO': 'Monday'
    }
    for day in days:
        if day in ds:
            ds = ds.replace(day, days[day])
    date = tz.localize(datetime.strptime(ds, '%A %d-%b-%Y %I:%M%p'))
    return date.astimezone(utc)


# See https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)