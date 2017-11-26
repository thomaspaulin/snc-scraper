import datetime
from typing import Dict

from snc.scraper.goal import Goal
from snc.scraper.penalty import Penalty
from snc.scraper.players import Goalie, Player
from snc.scraper.rink import Rink
from snc.scraper.team import Team


class MatchSummary:
    """Represents a match card and all the details that go with it. Includes all
        the information from a standard Match object (EXCEPT game type and
        season) and adds more such as the breakdown of goales, penalties, and
        even the players

        Attributes:
            start           The match start date and time
            rink            The match location
            away            The away team
            home            The home team
            away_score      The away team's score
            home_score      The home team's score

            goals           All the goals scored during the match
            shots           All the shots on goal taken during the match
            power_plays     The total number of power plays and the number of
                            successful power plays per team
            penalties       The penalites incurred during the match
            players         The players indexed by team
            goalies         The goalies indexed by team
    """
    def __init__(self,
                 *,
                 start: datetime,
                 rink: Rink,
                 away: Team,
                 home: Team,
                 away_score: int =0,
                 home_score: int =0,
                 goals: Dict[str, Goal]=None,
                 shots: Dict=None,
                 power_plays: Dict =None,
                 penalties: Dict[str, Penalty] =None,
                 players: Dict[str, Player]=None,
                 goalies: Dict[str, Goalie]=None):
        self.start = start
        self.rink = rink
        self.away = away
        self.home = home
        self.away_score = away_score
        self.home_score = home_score
        if goals is not None:
            self.goals = goals
        if shots is not None:
            self.shots = shots
        if power_plays is not None:
            self.power_plays = power_plays
        if penalties is not None:
            self.penalties = penalties
        if players is not None:
            self.players = players
        if goalies is not None:
            self.goalies = goalies

    def __str__(self):
        s = '{} - {} {} vs. {} {} at {}\n'.format(
                                                self.start,
                                                self.away.name,
                                                self.away_score,
                                                self.home_score,
                                                self.home.name,
                                                self.rink.name)
        s += '---------------------------------------------------\n'
        s += 'Goals: {}\n'.format(self.goals)
        s += 'Shots: {}\n'.format(self.shots)
        s += 'Penalties: {}\n'.format(self.penalties)
        s += 'Players: {}\n'.format(self.players)
        s += 'Goalies: {}\n'.format(self.goalies)
        return s

    def __repr__(self):
        return self.__str__()
