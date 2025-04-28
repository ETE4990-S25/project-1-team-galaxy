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