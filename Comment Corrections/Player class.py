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
   #saving player profile to dictionary
    def to_dict(self):
        return {
            "name": self.name, 
            "inventory": self.inventory,
            "health": self.health,
            "level": self.level,
            "credits": self.credits
        }