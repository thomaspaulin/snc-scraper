from enum import Enum
from datetime import time


class Goal:
    """Represents a Goal

    Attributes:
        type        The type of goal. Regular, power play, short handed
        period      Which period the goal was scorer in
        team        Team which scored
        time        When the goal was scored in seconds from the start of the
                    period
        scorer      The name of the player who scored the goal
        assisted_by The names of the players who assisted in the goal.
                    Up to two players can be listed. [] means unassisted
    """
    def __init__(self,
                 *,
                 type,
                 team,
                 period,
                 time,
                 scorer,
                 assisted_by=[]):
        self.type = type
        self.period = period
        self.team = team
        self.time = time
        self.scorer = scorer
        self.assisted_by = assisted_by

    def __str__(self):
        goal_time = time.strftime('%M:%S', self.time)
        s = 'Period {}, {} at {} - {}'.format(
                                            self.period,
                                            self.team,
                                            goal_time,
                                            self.scorer)
        if len(self.assisted_by) is 2:
            s += ' from {} and {}'.format(self.assisted_by[0],
                                          self.assisted_by[1])
        elif len(self.assisted_by) is 1:
            s += ' from {}'.format(self.assisted_by[0])
        else:
            s += ' (unassisted)'
        return s

    def __repr__(self):
        return '{}, {} at {} - {} assisted by {}'.format(
                                                    self.period,
                                                    self.team,
                                                    self.time,
                                                    self.scorer,
                                                    self.assisted_by)


class GoalType(Enum):
    REGULAR = 'RG'
    POWER_PLAY = 'PP'
    SHORTHANDED = 'SHG'
