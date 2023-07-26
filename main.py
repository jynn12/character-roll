import json
import random
from colorama import init, Fore, Style

def anime(file_path):
    try:
        with open(file_path, 'r') as anime_list:
            data = json.load(anime_list)
            char_list = data["characters"]
            random_name = random.choice(char_list)
            return random_name
    except FileNotFoundError:
        print(f"Error: JSON file '{file_path}' not found.")
        return None
    except KeyError:
        print(f"Error: JSON file '{file_path}' does not contain a 'characters' key.")
        return None

def print_color(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

if __name__ == "__main__":
    char_path = "anime.json"
    random_char = anime(char_path)
    if random_char:
        name = random_char["name"]
        age = int(random_char["age"])

        if 19 <= age <= 30:
            print(f"Your Character is {name}! Nice.", Fore.BLUE)

        elif 12 <= age <= 18:
            print_color(f"Your Character is {name}! But you are on FBI watchlist for interation with a minor.", Fore.YELLOW)

        elif 1 <= age <= 11:
            print(f"Your Character is {name}! WARNING, YOU ARE UNDER ARREST FOR PEDOPHILIA. SWAT TEAM IS ON THEIR WAY TO YOUR LOCATION.", Fore.RED)

        else:
            print(f"Your Character is {name}")
