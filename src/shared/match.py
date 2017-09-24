class Match:
    """
    Available keyword args:
        gametype, season, start, away, home, awayscore, homescore, rink
    """
    def __init__(self, **kwargs):
        self.gametype = kwargs.pop('gametype', None)
        self.season = kwargs.pop('season', None)
        self.start = kwargs.pop('start', None)
        self.away = kwargs.pop('away', None)
        self.home = kwargs.pop('home', None)
        self.awayscore = kwargs.pop('awayscore', None)
        self.homescore = kwargs.pop('homescore', None)
        self.rink = kwargs.pop('rink', None)

    def __str__(self):
        return '{},{},{},{},{},{},{},{}'.format(self.gametype, self.season, self.start, self.away, self.home,
                                                self.awayscore, self.homescore, self.rink)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def write_matches_csv(cls, matches, **kwargs):
        filename = kwargs.pop('filename', 'matches.csv')
        with open(filename, 'w') as f:
            for m in matches:
                f.write('%s\n' % m)

    @classmethod
    def read_from_csv(cls, **kwargs):
        filename = kwargs.pop('filename', 'matches.csv')
        matches = []
        with open(filename, 'r') as f:
            lines = f.readline()
            for line in lines:
                tokens = line.split(",")
                gametype = tokens[0]
                season = tokens[1]
                start = tokens[2]
                away = tokens[3]
                home = tokens[4]
                awayscore = tokens[5]
                homescore = tokens[6]
                rink = tokens[7]
                m = Match(gametype=gametype, season=season, start=start, away=away, home=home, awayscore=awayscore,
                          homescore=homescore, rink=rink)
                matches.append(m)
