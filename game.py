import random
import json
import os

class Player:
    def __init__(self, name, inventory = None, health=100, level=1, credits=100):
        self.name = name
        self.health = health
        self.level = level
        self.credits = credits
        self.inventory = inventory if inventory else []

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"Wow watch out... you just took {amount} damage! Your health us now {self.health}.")
    
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"Nice! You healed {amount}! Your health is now {self.health}.")

    def level_up(self):
        self.level += 1
        print(f"Oooooohh Yeah!, {self.name} just reached level {self.level}.")

    def show_inventory(self):
        if self.inventory:
            print(f"\n{self.name}'s Inventory:")
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item}")
        else:
            print("No Inventory")
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"you picked up: {item}")
    def to_dict(self):
        return {
            "name": self.name, 
            "inventory": self.inventory,
            "health": self.health,
            "level": self.level,
            "credits": self.credits
        }

class Planet:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.treasures = ["Plasma Shield", "Laser Sword", "Alien Blaster"]
        self.monsters = ["Alien Beast", "Space Serpent", "Galactic Raider"]
    
    def describe_planet(self):
        print(f"{self.name} is a mysterious planet with a difficulty of {self.difficulty}.")
    
    def explore(self, player):
        print(f"You have arrived on {self.name} (With a difficulty of: {self.difficulty})")
        if random.random() < 0.5:
            monster = random.choice(self.monsters)
            print(f"A {monster} appears!")

            action = input("Do you want to fight (yes/no)? ").strip().lower()
            if action =="yes":
                self.fight_monster(player, monster)
            else: 
                print("You avoided the fight and continued exploring.")
        else:
            print("You explore peacefully without encountering danger.")
            if random.random() < 0.5:
                found_item = random.choice(self.treasures)
                player.add_to_inventory(found_item)
                print(f"You found a hidden treasure: {found_item}.")

        #self.describe_planet()
        #chance_of_success = random.random()
        
        #if chance_of_success > self.difficulty * 0.2:
            #print("You have now concorded the PLANET!")
            #found_item = random.choice(self.treasures)
            #player.add_to_inventory(found_item)
            #if random.random() > 0.7:
                #self.encounter_monster(player)
        #else:
            #print("....This planet has to many extraturestials that you cannot defeat")
            #player.take_damage(20)
    
    def encounter_monster(self, player):
        print("A Alien monster has appeared!")
        monster = random.choice(self.monsters)
        print(f"You are face to face with a {monster}!")
        action = input("Do you want to fight or run? (fight/run): ").lower()
        if action == "fight":
            self.fight_monster(player, monster)
        elif action == "run":
            self.run_from_monster(player)
        else:
            print("Invalid action, The monster is eating you!")
            player.take_damage(20)
    
    def fight_monster(self, player, monster):
        monster_health = random.randint(30, 50)
        monster_reward = random.randint(20, 100)

        print(f"\nA wild {monster} has appeared with {monster_health} health!\n")

        while monster_health > 0 and player.health > 0:
            print("\n--- Battle Menu ---")
            print("1. Quick Attck (10-15 dmg, always hits)")
            print("2. Power Attack (20-30 dmg, 50 percent chance to hit)")
            print("3. Dodge (50 percent chance to avoid damage)")
            print("4. Run")

            action = input("choose an action: (1-4): ").strip()
            
            if action == "1":
                damage = random.randint(10,15)
                monster_health -= damage
                print(f"You attacked {monster} for {damage} damage! It has {monster_health} health left!")
            
            elif action == "2":
                if random.random() > 0.5:
                    damage = random.randint(20,30)
                    monster_health -= damage
                    print(f"Powerfull hit! You dealt {damage} damage! {monster} has {monster_health} HP left.")
                else: 
                    print("Your attack missed!")
            
            elif action == "3":
                if random.random() > 0.5:
                    print("You dodged the enemy attack!")
                    continue
                else:
                    print("Failed to dodge!")
            
            elif action == "4":
                print("You escaped safely!")
                break
            
            else:
                print("Invalid action. Monster attacked!")

            if monster_health > 0:
                monster_attack = random.randint(5, 15)
                player.take_damage(monster_attack)
                print(f"{monster} attacks you for {monster_attack} damage!")

        if player.health == 0:
            print("You have been conqured by the monster...")
       
        elif monster_health <= 0:
            print(f"You have defeated the {monster} and earned {monster_reward} credits!")
            player.credits += monster_reward
   
    def run_from_monster(self, player):
        chance_to_escape = random.random()
      
        if chance_to_escape > 0.5:
            print(f"You successfully escaped from the monster by a hair!")
       
        else:
            print("You couldn't escape in time! you are now the monsters food...")
            player.take_damage(20) 
       
    #maybe a def about the planet decription
class Galaxy:
    def __init__(self):
        self.planets = [
            Planet("Nebula", 1),
            Planet("Area 151", 2),
            Planet("Drull", 3),
        ]
    def show_planets(self):
        print("Planets among this galaxy:")
        for i, planet in enumerate(self.planets, 1):
            print(f"{i}. {planet.name} (Difficulty: {planet.difficulty})")
#need save and load functions
#use player_inventory.json for save and load

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

def load_game():
    save_files = [f for f in os.listdir() if f.startswith("player_") and f.endswith(".json")]
    if not save_files:
        print("\nNo saved games found. Starting a new game.")
        return None
    print("\nAvailable Saved Games: ")
    for i, file in enumerate(save_files, 1):
        print(f"{i}. {file}")

    try:
        choice = int(input("\nSelect a save file to load (Enter number): "))
        if 1 <= choice <= len(save_files):
            filename = save_files[choice - 1]
            with open(filename, "r") as file:
                data = json.load(file)
                player = Player(
                    name=data["name"], 
                    inventory=data.get("inventory", []),
                    health=data.get("health", 100),
                    level=data.get("level", 1),
                    credits=data.get("credits", 100)
                )
            print("\nGame loaded sucussefully from {filename}.")
            return player
        else:
            print("\nInvalid selection. Returning to main menu.")
            return None
    except ValueError:
        print("\nNo saved game found. Returning to main menu")
        return None
    except Exception as e:
        print(f"\nError loading game: {e}")
        return None
        
def load_inventory():
    try:
        with open('player_inventory.json', 'r') as file:
            inventory = json.load(file)
        return inventory
    except FileNotFoundError:
        print("Inventory file not found! Creating a new inventory.")
        return {"items": []}

# Function to save inventory data to JSON file
def save_inventory(inventory):
    with open('player_inventory.json', 'w') as file:
        json.dump(inventory, file)
    print("Inventory saved.")

def play_game(player, galaxy, shop):
    while True:
        print("\n=== Player Status ===")
        print(f"Name: {player.name}")
        print(f"Health: {player.health}")
        print(f"level: {player.level}")
        print(f"Credits: {player.credits}")
        print("\n--- Game Menu ---")
        print("1. Show Inventory")
        print("2. Explore Galaxy")
        print("3. Save Game")
        print("4. Save Inventory")
        print("5. Exit to Main Menu")
        print("6. Visit Space Shop")

        choice = input("Choose an option: ")
        if choice =="1":
            player.show_inventory()
        elif choice == "2":
            galaxy.show_planets()
            try:
                planet_choice = int(input("Select a planet to explore:  "))
                if 1 <= planet_choice <= len(galaxy.planets):
                    galaxy.planets[planet_choice - 1].explore(player)
                else:
                        print("\nInvalid planet selection.")
            except ValueError:
                    print("\nPlease enter a valid number.")
        elif choice == "3":
            save_character(player)
        elif choice == "4":
            save_inventory(player.to_dict())
        elif choice == "5":
            print("\nReturning to the main menu..")
            break
        elif choice == "6": 
            shop.buy_item(player)
        else:
            print("\nInvalid option. Try again.")
            
def main():
    print("Welcome to galaxy explore!")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. New Game")
        print("2. Load Game")
        print("3. Exit")
        choice = input("Choose an option: ")
       
        if choice == "1":
            player_name = input("\nEnter your name, explorer: ")
            player = Player(player_name)
            galaxy = Galaxy()
            shop = SpaceShop()
            
            print("\n=== Player Created! ===")
            print(f"Name: {player.name}")
            print(f"Health: {player.health}")
            print(f"Level: {player.level}")
            print(f"Credits: {player.credits}")
           
            play_game(player, galaxy, shop)

        elif choice == "2":
            player = load_game()
            if player:
                galaxy = Galaxy()
                shop = SpaceShop()
                play_game(player, galaxy, shop)
       
        elif choice == "3":
            print("\nSee you next time explorer! Safe travels!...watch for the space poop....")
       
        else:
            print("\nInvalid option. Select again.")

if __name__ == "__main__":
    main()

    