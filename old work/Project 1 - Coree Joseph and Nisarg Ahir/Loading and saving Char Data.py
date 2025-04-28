import json

# Function to load character data from JSON file
def load_character():
    try:
        with open('Character.json', 'r') as file:
            character = json.load(file)
        return character
    except FileNotFoundError:
        print("Character file not found! Please start a new game.")
        return None

# Function to save character data to JSON file
def save_character(character):
    with open('Character.json', 'w') as file:
        json.dump(character, file)
    print("Character data saved.")
