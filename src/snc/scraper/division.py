class Division:
    """A hockey division

    Attributes:
        name                The division's name
    """

    def __init__(self,
                 *,
                 name):
        self.name = name

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '{}'.format(self.name)
