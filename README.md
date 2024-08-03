# D&D 5E CLI Database Helper
![image](https://github.com/user-attachments/assets/2361af7b-b4bd-4141-99cd-13b7e80b2ac8)

Welcome adventurer! This command-line interface (CLI) tool is your guide to the vast world of Dungeons & Dragons 5th Edition. Easily search and explore spells, monsters, classes, and more by using the [D&D 5th Edition API](https://www.dnd5eapi.co/) -> [repo](https://github.com/5e-bits/5e-database) 

**Note**
This is a passion project while I actively study and work, so it won't get frequent updates.

## Features

* **Interactive Search:** Quickly find the information you need using fuzzy search.
* **Detailed Information:** Explore spells, monsters, classes, etc., with detailed descriptions and attributes.
* **Navigation:**  Dive into nested data structures to uncover even more details.
* **Stylized Output:**  Enjoy a colorful and eye-catching interface for a better user experience.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/momchilgeorgiev/dnd-5e-helper.git
2. **Install Dependencies:**
```bash
pip install requests prettytable prompt_toolkit colorama
```

## Usage
Open terminal and run:

```bash
python dnd_cli.py  
```

Select a Category: Use the fuzzy search to choose a category (e.g., spells, monsters).

Select an Item: Narrow down your search by selecting a specific item from the chosen category.

Explore Details: Navigate through the item's attributes and subfields using the interactive prompts.

**Examples**

- **Find a Spell:** Select "spells" as the category and then search for "fireball".
- **View Monster Stats:** Explore the abilities and features of a "beholder" under the "monsters" category.
- **Discover Class Features:** Dive into the features and subclasses of the "rogue" class.

### Sources
- [Image source link](https://www.dicebreaker.com/games/dungeons-and-dragons-5e/feature/dnd-shadow-dragon-queen-warriors-krynn-preview)
