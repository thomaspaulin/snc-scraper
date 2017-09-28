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
                 number,
                 name,
                 position):
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
                 number,
                 name):
        self.number = number
        self.name = name

    def __str__(self):
        return '#{} {} G'.format(self.number, self.name)

    def __repr__(self):
        return self.__str__()
