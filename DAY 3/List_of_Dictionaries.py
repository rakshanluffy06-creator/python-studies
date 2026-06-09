players = [
    {"id": 1, "name": "rocky", "sport": "Cricket"},
    {"id": 2, "name": "maari", "sport": "Football"},
    {"id": 3, "name": "leo", "sport": "Badminton"}
]

for p in players:
    print(f"[{p['id']}] {p['name']} - {p['sport']}")


# Function Returning a Dictionary

def register_player(name, age, sport):
    return {
        "name": name,
        "age": age,
        "sport": sport
    }

player = register_player("yash", 21, "Cricket")

print(player)
