import time
from enum import Enum
from typing import List

from snc.scraper.players import Player
from snc.scraper.team import Team


class Goal:
    """Represents a Goal

    Attributes:
        type        The type of goal. Regular, power play, short handed
        period      Which period the goal was scorer in
        team        Team which scored
        time        When the goal was scored in seconds from the start of the
                    period as a string
        scorer      The name of the player who scored the goal
        assisted_by The names of the players who assisted in the goal.
                    Up to two players can be listed.
    """
    def __init__(self,
                 *,
                 goal_type: GoalType,
                 team: str,
                 period: int,
                 goal_time: int,
                 scorer: str,
                 assisted_by: List[str]=None):
        # todo type the parameters to Team and Player rather than str
        self.type = goal_type
        self.period = period
        self.team = team
        try:
            self.time = time.strptime(goal_time, '%M:%S')
        except ValueError:
            print('Failed to parse the time: {}'.format(goal_time))
            self.time = None
        self.scorer = scorer
        self.assisted_by = assisted_by

    def __str__(self):
        goal_time = time.strftime('%M:%S', self.time)
        s = 'Period {}, {} at {} - {}'.format(
                                            self.period,
                                            self.team,
                                            goal_time,
                                            self.scorer)
        if self.assisted_by is None:
            s += ' (unassisted)'
        elif len(self.assisted_by) is 2:
            s += ' from {} and {}'.format(self.assisted_by[0],
                                          self.assisted_by[1])
        elif len(self.assisted_by) is 1:
            s += ' from {}'.format(self.assisted_by[0])

        return s

    def __repr__(self):
        return self.__str__()


class GoalType(Enum):
    REGULAR = 'RG'
    POWER_PLAY = 'PP'
    SHORTHANDED = 'SHG'
