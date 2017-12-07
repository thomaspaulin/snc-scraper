BASE_URL: str = 'http://www.aucklandsnchockey.com'
API_URL: str = 'https://snc-api.herokuapp.com/api/v0'

LEAGUES_URL: str = '{}/leagues'.format(BASE_URL)
SCHEDULES_URL: str = '{}/schedules.cfm?clientID=5857&leagueID=23670'.format(LEAGUES_URL)
PRINTABLE_SCHEDULE_URL: str = '{}/print_schedule.cfm?leagueID=23341&clientID=5788&teamID=0&mixed=1'.format(LEAGUES_URL)
TEAMS_URL: str = '{}/teams.cfm?leagueID=23341&clientID=5788'.format(LEAGUES_URL)
