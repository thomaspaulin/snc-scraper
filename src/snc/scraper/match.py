from enum import Enum
from datetime import datetime
import snc.scraper.parsing_utils as util


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
        self.game_type = game_type
        self.season = season
        if str(start):
            self.start = util.parse_date(start, '%Y-%m-%dT%H:%M:%SZ')
        else:
            self.start = start
        self.away = away
        self.home = home
        self.away_score = away_score
        self.home_score = home_score
        self.rink = rink

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

    @classmethod
    def write_matches_csv(cls, matches, **kwargs):
        filename = kwargs.pop('filename', 'matches.csv')
        with open(filename, 'w') as f:
            for m in matches:
                f.write('%s\n' % m)

    @classmethod
    def read_from_csv(cls, **kwargs):
        filename = kwargs.pop('filename', 'matches.csv')
        matches = []
        with open(filename, 'r') as f:
            lines = f.readline()
            for line in lines:
                tokens = line.split(",")
                gametype = tokens[0]
                season = int(tokens[1])
                start = tokens[2]
                away = tokens[3]
                home = tokens[4]
                awayscore = tokens[5]
                homescore = tokens[6]
                rink = tokens[7]
                m = Match(
                        game_type=gametype,
                        season=season,
                        start=start,
                        away=away,
                        home=home,
                        away_score=awayscore,
                        home_score=homescore,
                        rink=rink)
                matches.append(m)
