class Team:
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.logo_url = kwargs.pop('logo_url', None)
        self.record = kwargs.pop('record', (0, 0, 0))

    def __str__(self):
        return '{} {}'.format(self.name, self.record)

    def __repr__(self):
        return '{}, {}, {}'.format(self.name, self.logo_url, self.record)
