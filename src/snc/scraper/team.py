class Team:
    """A hockey Team

    Attributes:
        name                The team's name
        division            The division the team is in
        logo_url            The URL of the team's logo
        record              The wins, loses, ties, of the team for the season
        points              How many points the team has. Based of their record
                            for the reason and point allocation
                            (see __pointAllocation)

        __pointAllocation   [private] The points for a win, lose, and tie, respectively
    """
    __pointAllocation = (3, 0, 1)

    def __init__(self,
                 *,
                 name,
                 division_name=None,
                 logo_url=None,
                 record=(0, 0, 0),
                 points=0):
        self.name = name
        self.division_name = division_name
        self.logo_url = logo_url
        self.record = record
        if points > 0:
            self.points = points
        else:
            self.points = (
                record[0] * self.__pointAllocation[0]
                + record[1] * self.__pointAllocation[1]
                + record[2] * self.__pointAllocation[2]
            )

    def dump(self):
        return {'name': self.name,
                'divisionName': self.division_name,
                'logoURL': self.logo_url}

    @staticmethod
    def load(json):
        try:
            logo_url: str = json['logoURL']
        except KeyError:
            logo_url: str = ''
        try:
            div_name: str = json['divisionName']
        except KeyError:
            div_name: str = 'Unknown'
        return Team(name=json['name'],
                    division_name=div_name,
                    logo_url=logo_url)

    def __str__(self):
        return '{} {}'.format(self.name, self.record)

    def __repr__(self):
        return '{}, Division {}, {}, {} - {}pts'.format(
                                        self.name,
                                        self.division_name,
                                        self.logo_url,
                                        self.record,
                                        self.points)
