import requests
from prettytable import PrettyTable
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from textwrap import wrap
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Initialize colorama

API_BASE_URL = "https://www.dnd5eapi.co/api"

def print_title():
    f= open ('logo.txt','r')
    print(''.join([line for line in f]))

def get_api_data(endpoint):
    url = f"{API_BASE_URL}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(Fore.RED + f"Error fetching data from {url}" + Style.RESET_ALL)
        return None

def display_categories(categories):
    table = PrettyTable()
    table.field_names = [Fore.GREEN + Style.BRIGHT + "Categories" + Style.RESET_ALL]
    table.align = "l"
    for category in categories:
        table.add_row([Fore.CYAN + category + Style.RESET_ALL])
    print(table)

def fuzzy_search(options, prompt_text):
    completer = FuzzyWordCompleter(options)
    return prompt(prompt_text, completer=completer)

def wrap_text(text, width=60):
    if isinstance(text, list):
        return [item for sublist in [wrap(t, width=width) for t in text] for item in sublist]
    return wrap(str(text), width=width)

def display_item_details(item_data, key_prefix=""):
    table = PrettyTable()
    table.field_names = [Fore.GREEN + Style.BRIGHT + "Attribute" + Style.RESET_ALL, 
                         Fore.GREEN + Style.BRIGHT + "Value" + Style.RESET_ALL]
    table.align = "l"
    table.max_width = 60

    for key, value in item_data.items():
        full_key = f"{key_prefix}{key}"
        if isinstance(value, (str, int, float, bool)):
            table.add_row([Fore.CYAN + full_key.capitalize() + Style.RESET_ALL, 
                           Fore.WHITE + "\n".join(wrap_text(str(value))) + Style.RESET_ALL])
        elif isinstance(value, list) and all(isinstance(x, (str, int, float, bool)) for x in value):
            table.add_row([Fore.CYAN + full_key.capitalize() + Style.RESET_ALL, 
                           Fore.WHITE + "\n".join(wrap_text(value)) + Style.RESET_ALL])
        elif isinstance(value, dict) or (isinstance(value, list) and any(isinstance(x, dict) for x in value)):
            table.add_row([Fore.CYAN + full_key.capitalize() + Style.RESET_ALL, 
                           Fore.YELLOW + "(Nested data)" + Style.RESET_ALL])

    print(table)

def explore_item(item_data, path=""):
    while True:
        display_item_details(item_data, path)
        
        options = list(item_data.keys()) + ['..', 'back']
        choice = fuzzy_search(options, f"Select a field to explore (or '..' to go up, 'back' to main menu): ")

        if choice == 'back':
            return False
        elif choice == '..':
            return True
        elif isinstance(item_data[choice], dict):
            if not explore_item(item_data[choice], f"{path}{choice}."):
                return False
        elif isinstance(item_data[choice], list) and any(isinstance(x, dict) for x in item_data[choice]):
            print(Fore.MAGENTA + f"\n{choice}:" + Style.RESET_ALL)
            for i, item in enumerate(item_data[choice]):
                if isinstance(item, dict):
                    print(Fore.YELLOW + f"Item {i + 1}:" + Style.RESET_ALL)
                    display_item_details(item, f"{path}{choice}[{i}].")
                else:
                    print(Fore.CYAN + f"Item {i + 1}: " + Fore.WHITE + f"{item}" + Style.RESET_ALL)
            input(Fore.GREEN + "Press Enter to continue..." + Style.RESET_ALL)
        else:
            print(Fore.MAGENTA + f"\n{choice}:" + Style.RESET_ALL)
            print(Fore.WHITE + "\n".join(wrap_text(item_data[choice])) + Style.RESET_ALL)
            input(Fore.GREEN + "Press Enter to continue..." + Style.RESET_ALL)

def main():
    categories = [
        "ability-scores", "alignments", "backgrounds", "classes", 
        "conditions", "damage-types", "equipment", "equipment-categories", 
        "feats", "features", "languages", "magic-items", "magic-schools", 
        "monsters", "proficiencies", "races", "rule-sections", "rules", 
        "skills", "spells", "subclasses", "subraces", "traits", "weapon-properties"
    ]

    print_title()
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to the D&D 5e CLI DB Helper!" + Style.RESET_ALL)
    
    while True:
        display_categories(categories)
        category = fuzzy_search(categories, "Select a category (or type 'exit' to quit): ")

        if category.lower() in ['exit', 'quit', 'q']:
            print(Fore.MAGENTA + Style.BRIGHT + "Thank you for using the D&D 5e CLI DB Helper. May your adventures be legendary!" + Style.RESET_ALL)
            break

        category_data = get_api_data(category)
        if not category_data:
            continue

        items = [item['index'] for item in category_data['results']]
        item = fuzzy_search(items, f"Select a {category} item: ")

        item_data = get_api_data(f"{category}/{item}")
        if item_data:
            explore_item(item_data)

if __name__ == "__main__":
    main()