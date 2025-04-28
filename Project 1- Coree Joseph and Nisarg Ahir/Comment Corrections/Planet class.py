class Planet:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.treasures = ["Plasma Shield", "Laser Sword", "Alien Blaster"]
        self.monsters = ["Alien Beast", "Space Serpent", "Galactic Raider"]
    
    def describe_planet(self):
        print(f"{self.name} is a mysterious planet with a difficulty of {self.difficulty}.")
    #option to choose fight or not
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
    #this is where player gets to fight monster while showing monster and player health and attack points
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
       