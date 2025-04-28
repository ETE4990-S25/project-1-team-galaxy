class SpaceShop:
    def __init__(self):
        self.items = {
            "Health Potion": 50,
            "Laser Sword": 150,
            "Shield Generator": 100,
            "Energy Pack":75
        }
    def display_shop(self):
        print("\n --- Welcome to the Space Shop ---" )
        for item, price in self.items.items():
            print(f"{item}: {price} credits")

    def buy_item(self, player):
        self.display_shop()
        choice = input("Enter the item name you want to buy (or 'exit' to leave): ").title()
        if choice in self.items:
            if player.credits >= self.items[choice]:
                player.credits -= self.items[choice]
                player.add_to_inventory(choice)
                print(f"You purchased {choice} for {self.items[choice]} credit.")
            else: 
                print("You don't have enough credits")
        elif choice.lower() == "exit":
            print("Leaving the shop...")
        else:
            print("Invalid selection...")

def save_character(player):
    try: 
        filename = f"player_{player.name}.json"
        with open(filename, "w") as file:
            json.dump(player.to_dict(), file)
        print("\nGame save Successful")
    except Exception as e:
        print(f"\nError saving game: {e}")