player = {
    "name": "guna",
    "age": 23,
    "sport": "Cricket",
    "team": "Chennai Kings"
}

# Update existing value
player["active"] = True

# Add new key
player["position"] = "Batsman"

# Delete a key
del player["team"]

print(player)
