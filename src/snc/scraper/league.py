class League:
    """A hockey league

    Attributes:
        name                The league's name
    """

    def __init__(self,
                 *,
                 name: str):
        self.name = name

    def dump(self):
        return self.__dict__

    @staticmethod
    def load(json):
        return League(name=json['name'])

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '{}'.format(self.name)
