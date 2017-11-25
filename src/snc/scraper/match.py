import pytz
from datetime import datetime, timedelta
from enum import Enum

import snc.scraper.parsing_utils as util
from snc.scraper.division import Division


class MatchType(Enum):
    PRACTICE = 'PR'
    REGULAR_SEASON = 'RS'
    PLAYOFF = 'PO'


class Match:
    """A hockey match

    Attributes:
        game_type   The game's type. Typically practice, regular season, or
                    playoff. PR, RO, and PO respectively
        season      The season the match is in
        start       The datetime at which the match starts, in UTC. Otherwise a date string in the format
                    2017-09-30T19:00:55Z
        away        The away team
        home        The home team
        away_score  The away team's score. None if the game hasn't been played
        home_score  The home team's score. None if the game hasn't been played
        rink        Where the match was played
    """
    def __init__(self,
                 *,
                 game_type=MatchType.REGULAR_SEASON,
                 season=datetime.utcnow().year,
                 start=datetime.utcnow(),
                 away,
                 home,
                 away_score=None,
                 home_score=None,
                 rink):

        now = datetime.utcnow()
        if type(game_type) is str:
            for name, value in [(e.name, e.value) for e in MatchType]:
                if value == game_type:
                    self.game_type = MatchType[name]
                    break
                else:
                    self.game_type = MatchType.REGULAR_SEASON
        else:
            self.game_type = game_type
        self.season = season
        if type(start) is str:
            self.start = util.parse_date(start, '%Y-%m-%dT%H:%M:%SZ')
        else:
            self.start = start
        if start + timedelta(hours=1) < now.replace(tzinfo=pytz.UTC):
            self.status = "Over"
        elif start <= now.replace(tzinfo=pytz.UTC) and start + timedelta(hours=1) <= now.replace(tzinfo=pytz.UTC):
            self.status = "Underway"
        else:
            self.status = "Upcoming"
        self.away = away
        self.home = home
        if away.division is not None:
            self.division = away.division
        elif home.division is not None:
            self.division = home.division
        else:
            self.division = Division(name='Unknown')
        self.away_score = away_score
        self.home_score = home_score
        self.rink = rink

    def dump(self):
        time = datetime.strftime(self.start, '%Y-%m-%dT%H:%M:%SZ')
        return {'start': time,
                'season': self.season,
                'status': self.status,
                'division': self.division.dump(),
                'away': self.away.dump(),
                'home': self.home.dump(),
                'awayScore': self.away_score,
                'homeScore': self.home_score,
                'rink': self.rink.dump()}

    @staticmethod
    def load(json):
        # todo
        pass

    def __str__(self):
        time = datetime.strftime(self.start, '%Y-%m-%dT%H:%M:%SZ')
        return '{},{},{},{},{},{},{},{}'.format(
                                            self.game_type,
                                            self.season,
                                            time,
                                            self.away,
                                            self.home,
                                            self.away_score,
                                            self.home_score,
                                            self.rink)

    def __repr__(self):
        return self.__str__()
