def load_inventory():
    try:
        with open('player_inventory.json', 'r') as file:
            inventory = json.load(file)
        return inventory
    except FileNotFoundError:
        print("Inventory file not found! Creating a new inventory.")
        return {"items": []}