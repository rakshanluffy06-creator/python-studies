players = ["virat", "dhoni", "dube"]

for player in players:
    print("Player:", player)


players = ["bens", "shami", "siraj"]

for index, player in enumerate(players, start=1):
    print(f"{index}. {player}")


count = 0
max_players = 3

while count < max_players:
    print(f"Registering Player #{count + 1}")
    count += 1

print("Registration Closed")
