import time


class Penalty:
    """Represents a penalty

    Attributes:
        offense     Type of penalty
        period      The period during which the penalty was incurred
        time        Time of the penalty in seconds from the start of the period
                    as a string
        team        Team of the offending player
        offender    The offending player's name
        pim         Penalty incurred minutes
    """
    def __init__(self,
                 *,
                 offense,
                 period,
                 penalty_time,
                 team,
                 offender,
                 pim=2):
        self.offense = offense
        self.period = period
        self.time = time.strptime(penalty_time, '%M:%S')
        self.team = team
        self.offender = offender
        self.pim = pim

    def __str__(self):
        penalty_time = time.strftime('%M:%S', self.time)
        return '{} at {} - {} for {} ({} mins)'.format(
                                                self.team,
                                                penalty_time,
                                                self.offender,
                                                self.offense,
                                                self.pim)

    def __repr__(self):
        return self.__str__()
