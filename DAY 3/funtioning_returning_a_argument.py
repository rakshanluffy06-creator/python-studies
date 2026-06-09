def register_player(name, age, team):
    return {
        "player_name": name,
        "age": age,
        "team": team
    }

player = register_player("santhosh", 21, "Chennai Kings")

print(player)
