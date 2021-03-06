class Player:
    """An person playing as a forward or defenceman

    Attributes:
        number      Jersey number
        name        Name
        position    Either F or D

    Other information coming later
    """
    def __init__(self,
                 *,
                 number: int,
                 name: str,
                 position: str ='?'):
        self.number = number
        self.name = name
        self.position = position

    def __str__(self):
        return '#{} {} {}'.format(self.number, self.name, self.position)

    def __repr__(self):
        return self.__str__()


class Goalie:
    """A goalie

    Attributes:
        number      Jersey number
        name        Name

    Other informatin coming later
    """
    def __init__(self,
                 *,
                 number: int,
                 name: str,
                 mins: int = 0,
                 shots_faced: int = 0,
                 saves_made: int = 0):
        self.number = number
        self.name = name
        self.mins = mins
        self.shots_faced = shots_faced
        self.saves_made = saves_made
        self.save_pct: float = saves_made / shots_faced

    def __str__(self):
        return '#{} {} G'.format(self.number, self.name)

    def __repr__(self):
        return self.__str__()
