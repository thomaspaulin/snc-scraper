# For scraping http://www.aucklandsnchockey.com/leagues/hockey_boxscores_printable.cfm?clientID=5788&leagueID=23341&gameID=[some-id-here]
# That is, it is for scraping the match information

def parse_teams(elem):
    """Returns the teams involved in the match"""
    pass

def parse_goals(elem):
    """Returns all the goals scored indexed by team"""
    pass

def parse_shots(elem):
    """Returns all the shots on goal indexed by team"""
    pass

def parse_power_plays(elem):
    """Returns the a tuple of the successful power plays and total power plays
    in a dictionary indexed by team
    """
    pass

def parse_details(elem):
    """Returns the match details in a dictionary"""
    pass

def parse_penalties(elem):
    """Returns the penalties indexed by team"""
    pass

def parse_players(elem):
    """Returns a list of players"""
    pass

def parse_goalies(elem):
    """Returns a list of goalies"""
    pass

def parse_page(soup):
    """Returns a MatchSummary object that represents the given box score page"""
    teams = parse_teams()
    goals = parse_goals()
    shots_on_goal = parse_shots()
    power_plays = parse_power_plays()
    details = parse_details()
    penalies = parse_penalties(teams)
    away_players = parse_players()
    home_players = parse_players()
    away_goalies = parse_goalies()
    home_goalies = parse_goalies()
