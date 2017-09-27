class Team:
    """A hockey Team

    Attributes:
        name                The team's name
        logo_url            The URL of the team's logo
        record              The wins, loses, ties, of the team for the season
        points              How many points the team has. Based of their record
                            for the reason and point allocation
                            (see __pointAllocation)

        __pointAllocation   [private] The points for a win, lose, and tie,
                            respectively
    """
    __pointAllocation = (3, 0, 1)

    def __init__(self, *, name, logo_url, record=(0, 0, 0), points=0):
        self.name = name
        self.logo_url = logo_url
        self.record = record
        self.points = record[0] * __pointAllocation[0] + record[1] * __pointAllocation[1] + record[2] * __pointAllocation[2]

    def __str__(self):
        return '{} {}'.format(self.name, self.record)

    def __repr__(self):
        return '{}, {}, {} - {}pts'.format(self.name, self.logo_url, self.record, self.points)
