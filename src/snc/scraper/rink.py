class Rink:
    def __init__(self, *, name):
        self.name = name

    def dump(self):
        return {'name': self.name}

    def __str__(self):
        return '{} rink'.format(self.name)

    def __repr__(self):
        return self.__str__()