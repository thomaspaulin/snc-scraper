from datetime import datetime
from pytz import timezone, utc


def capitalise(string):
    words = string.strip().lower().split(' ')
    upper_words = []
    for word in words:
        upper_words.append(word[0:1].upper() + word[1:])
    return ' '.join(upper_words)


def parse_date(date_str, str_format):
    tz = timezone("Pacific/Auckland")
    return tz.localize(datetime.strptime(date_str, str_format))


def parse_int(str, default):
    try:
        return int(str)
    except ValueError:
        return default
