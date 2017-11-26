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
        pim         Penalty infraction minutes
    """
    def __init__(self,
                 *,
                 offense: str,
                 period: int,
                 penalty_time: int,
                 team: str,
                 offender: str,
                 pim: int = 2):
        # todo type team and offender properly
        self.offense = offense
        self.period = period
        try:
            self.time = time.strptime(penalty_time, '%M:%S')
        except ValueError:
            print('Failed to parse the time: {}'.format(penalty_time))
            self.time = None
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
