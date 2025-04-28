def save_character(player):
    try: 
        filename = f"player_{player.name}.json"
        with open(filename, "w") as file:
            json.dump(player.to_dict(), file)
        print("\nGame save Successful")
    except Exception as e:
        print(f"\nError saving game: {e}")