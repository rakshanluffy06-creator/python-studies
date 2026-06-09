player = {
    "player_name": "gohan",
    "age": 21,
    "team": "covai kings",
    "game": "Cricket",
    "active": True
}

print(player)

# Accessing Values
print(player["player_name"])      
print(player["game"])             
print(player.get("position", "Assigned"))
