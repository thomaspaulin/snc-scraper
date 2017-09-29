from enum import Enum
import time


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
                 goal_type,
                 team,
                 period,
                 goal_time,
                 scorer,
                 assisted_by=None):
        self.type = goal_type
        self.period = period
        self.team = team
        self.time = time.strptime(goal_time, '%M:%S')
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
