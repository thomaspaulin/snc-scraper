from datetime import datetime
from pytz import timezone, utc


def capitalise(string):
    words = string.strip().lower().split(' ')
    upper_words = []
    for word in words:
        print(word[0:1].upper() + word[1:])
        upper_words.append(word[0:1].upper() + word[1:])
    return ' '.join(upper_words)


def parse_date(date_str, str_format, timezone):
    tz = timezone("Pacific/Auckland")
    return tz.localize(datetime.strptime(date_str, str_format))
