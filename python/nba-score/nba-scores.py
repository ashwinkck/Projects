from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

printer = PrettyPrinter()

# Add a standard browser User-Agent header to bypass the anti-bot block
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.nba.com/"
}

# Pass the headers into the get request
response = get(BASE_URL, headers=HEADERS)

# Optional debugging safety guard
if response.status_code != 200:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

data = response.json()

scoreboard = data["scoreboard"]
games = scoreboard["games"]

def getGames():
    print(scoreboard['gameDate'])
    print('''-------------------------------------''')
    for game in games:
        homeTeam = game['homeTeam']
        awayTeam = game['awayTeam']
        homeScore = homeTeam['score']
        awayScore = awayTeam['score']
        period = game['period']
        if period == 0:
            homeScore = ""
            awayScore = ""
        clock = game['gameClock']
        if clock == "":
            clock = 0
        status = game['gameStatusText']
        leaders = game['gameLeaders']
        hLeaders = leaders['homeLeaders']
        aLeaders = leaders['awayLeaders']
        print(f'''{homeTeam['teamCity']} {homeTeam['teamName']} {homeScore} 
VS 
{awayTeam['teamCity']} {awayTeam['teamName']} {awayScore}''')
        print(f"{status}")
        if status == "Final":
            print(f'''Game Leaders: 
Home: {hLeaders['jerseyNum']} {hLeaders['name']} 
Away: {aLeaders['jerseyNum']} {aLeaders['name']}''')
        print('''-------------------------------------''')
        
getGames()
