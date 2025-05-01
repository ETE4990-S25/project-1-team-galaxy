def save_inventory(inventory):
    with open('player_inventory.json', 'w') as file:
        json.dump(inventory, file)
    print("Inventory saved.")