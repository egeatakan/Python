import csv

PLAYERS = 'players.csv'
GAMES = 'games.csv'

def delta(winner, loser):
    return 1 / (1 + 2**((winner - loser) / 100))

def read_players(filename):
    players = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                players[row['PLAYER']] = int(row['SELO'])
    except OSError as problem:
        print(f"Eyvah {problem}")
    return players

def elo_win(winner, loser):
    d = delta(winner,loser)
    winner += 200 * d
    loser -= 200 * d
    #print(200*d)
    return round(winner), round(loser)

def update_elo(db, name1, name2, result):
    if result == '1-0':
        db[name1], db[name2] = elo_win(db[name1], db[name2])
    elif result == '0-1':
        db[name2], db[name1] = elo_win(db[name2], db[name1])
    
def main():
        players = read_players(PLAYERS)

        try:
            with open(GAMES, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['PLAYER A'] not in players:
                        players[row['PLAYER A']] = 1500
                    if row['PLAYER B'] not in players:
                        players[row['PLAYER B']] = 1500
                    update_elo(players,row['PLAYER A'],row['PLAYER B'],row['RESULT'])                    
        except OSError as sorun:
            print(f"eyvah {sorun}")

        for p in sorted(players, key=lambda p: players[p], reverse=True):  
          print(f"{p} : {players[p]}")

if __name__ == '__main__':
    main()

