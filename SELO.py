import csv
PLAYERS = "players.csv"
GAMES = "games.csv"


def delta(player_1, player_2):
    return 1 / (1 + 2**((player_1 - player_2) / 100))


def main():
    selo_scores = {}
    with open(PLAYERS, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            selo_scores[row['PLAYER']] = int(row['SELO'])

    with open(GAMES, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_a = row['PLAYER A']
            player_b = row['PLAYER B']
            result = row['RESULT']

            selo_a = selo_scores.get(player_a, 1500)
            selo_b = selo_scores.get(player_b, 1500)

            if result == '1-0':
                change = round(200 *delta(selo_a,selo_b))
                selo_scores[player_a] = selo_a + change
                selo_scores[player_b] = selo_b - change
            elif result == '0-1':
                change = round(200 * delta(selo_b,selo_a))
                selo_scores[player_b] = selo_b + change
                selo_scores[player_a] = selo_a - change

    sorted_selo = sorted(selo_scores.items())

    for player,selo in sorted_selo:
        print(f"{player} : {selo}")

if __name__ == "__main__":
 main()