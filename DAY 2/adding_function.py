ADDING A ITEMS:

players = ["virat"]
players.append("dhoni")
players.insert(0, "rohit")

print(players)

FUNCTION WITH LIST:
def show_players(player_list):
    print("Total Players:", len(players_list))

    for player in player_list:
        print("-", player)

my_players = ["virat", "dhoni", "rohit"]

show_patients(my_players)
