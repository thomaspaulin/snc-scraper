class Division:
    """A hockey division

    Attributes:
        name                The division's name
    """

    def __init__(self,
                 *,
                 name: str):
        self.name = name

    def dump(self):
        return self.__dict__

    @staticmethod
    def load(json):
        return Division(name=json['name'])

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '{}'.format(self.name)
