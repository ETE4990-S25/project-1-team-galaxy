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