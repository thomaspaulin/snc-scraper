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

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.logo_url = kwargs.pop('logo_url', None)
        self.record = kwargs.pop('record', (0, 0, 0))
        self.points =

    def __str__(self):
        return '{} {}'.format(self.name, self.record)

    def __repr__(self):
        return '{}, {}, {}'.format(self.name, self.logo_url, self.record)
