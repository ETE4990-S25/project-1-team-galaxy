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