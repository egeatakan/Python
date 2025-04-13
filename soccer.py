CSV_FILE = 'player_stats.csv'
text_fields =('player','position','team')

import csv

def read_players_stats(filename):
    players = list()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for k,v in row.items():
                if k not in text_fields:
                    row[k] = int(v)
            players.append(row)
        return players
    

def calculate_efficiencies(players):
    for p in players:
        p['forward_efficiency'] = (p['goals'] + p['assists'] - p['offsides']) / p['minutes']
        if p['crosses'] == 0:
            t = 0
        else:
            t = p['assists'] / p['crosses']
        p['midfield_efficiency'] = (p['interceptions'] + p['ball_recoveries'] + t) / p['minutes']

def split_teams(players):
    teams = dict()
    for p in players:
        if p['team'] not in teams:
            teams[p['team']] = list()
        teams[p['team']].append(dict(p))
    return teams


def main():
    players = read_players_stats(CSV_FILE)
    calculate_efficiencies(players)

    print(f"{'Name':<30s} {'Team':<30s} {'Forward efficiency':>20s}")
    for p in sorted(players, key=lambda p: p['forward_efficiency'], reverse=True)[:3]:
        print(f"{p['player']:<30s} {p['team']:<30s} {p['forward_efficiency']:20.3f}")
    print()

    print(f"{'Name':<30s} {'Team':<30s} {'Midfield Efficiency':>20s}")
    for p in sorted(players, key=lambda p: p['midfield_efficiency'], reverse=True)[:3]:
        print(f"{p['player']:<30s} {p['team']:<30s} {p['midfield_efficiency']:20.3f}")
    print()

    all_teams = split_teams(players)

    total_age=dict()
    for team, team_players in all_teams.items():
        total_age[team] = list()
        for player in sorted(players, key=lambda p: p['birth_year']):
            total_age[team].append(2025 - player['birth_year'])
        
    avg_age = []
    for team, ages in total_age.items():
        avg_age[team] = sum(ages) / len(ages)
    print("The three teams with lower age average are:")
    for t, a in sorted(avg_age.items(), key=lambda x: x[1])[:3]:
        print(f"{t:<30} {a:.2f} years")
    print()

    
    #efficiency_tot = dict()
   # efficiency_players = dict()
  #  for team,team_players in all_teams.items():
 #       efficiency_tot[team] = 0
#       efficiency_players[team] = list()
#        for p in sorted(team_players, key=lambda x: x[1])[:3]:
            
if __name__ == "__main__":
    main()