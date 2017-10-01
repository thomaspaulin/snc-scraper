
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
                 start,
                 rink,
                 away,
                 home,
                 away_score=0,
                 home_score=0,
                 goals=None,
                 shots=None,
                 power_plays=None,
                 penalties=None,
                 players=None,
                 goalies=None):
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
                                                self.away,
                                                self.away_score,
                                                self.home_score,
                                                self.home,
                                                self.rink)
        s += '---------------------------------------------------\n'
        s += 'Goals: {}\n'.format(self.goals)
        s += 'Shots: {}\n'.format(self.shots)
        s += 'Penalties: {}\n'.format(self.penalties)
        s += 'Players: {}\n'.format(self.players)
        s += 'Goalies: {}\n'.format(self.goalies)
        return s

    def __repr__(self):
        return self.__str__()
