from enum import Enum

class Goal:
    """Represents a Goal

    Attributes:
        type        The type of goal. Regular, power play, short handed
        period      Which period the goal was scorer in
        time        When the goal was scored in seconds from the start of the
                    period
        scorer      The name of the player who scored the goal
        assisted_by The names of the players who assisted in the goal. Up to two
                    players can be listed. None means unassisted
    """
    def __init__(self, *, type, period, time, scorer, assisted_by=None):
        self.type = type
        self.period = period
        self.time = time
        self.scorer = scorer
        self.assisted_by = assisted_by

class GoalType(Enum):
    REGULAR = 'RG'
    POWER_PLAY = 'PP'
    SHORTHANDED = 'SHG'
