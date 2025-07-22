import random
import string
import json
import time

# Constants
CREATURE_TYPES = ['Dragon', 'Goblin', 'Elf', 'Troll', 'Phoenix', 'Golem', 'Hydra', 'Griffin']
ELEMENTS = ['Fire', 'Water', 'Earth', 'Air', 'Shadow', 'Light', 'Ice', 'Lightning']
ADJECTIVES = ['Ancient', 'Mystic', 'Savage', 'Noble', 'Cursed', 'Divine', 'Feral', 'Ethereal']

# Creature class
class Creature:
    def __init__(self, name, ctype, element, strength, agility, intelligence):
        self.name = name
        self.ctype = ctype
        self.element = element
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def power_level(self):
        return self.strength * 1.5 + self.agility + self.intelligence * 1.2

    def to_dict(self):
        return {
            'name': self.name,
            'type': self.ctype,
            'element': self.element,
            'strength': self.strength,
            'agility': self.agility,
            'intelligence': self.intelligence,
            'power_level': self.power_level()
        }

    def __str__(self):
        return f"{self.name} the {self.element} {self.ctype} (STR: {self.strength}, AGI: {self.agility}, INT: {self.intelligence})"

# Utility functions
def random_name():
    return ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 7)))

def generate_creature():
    name = random.choice(ADJECTIVES) + " " + random_name()
    ctype = random.choice(CREATURE_TYPES)
    element = random.choice(ELEMENTS)
    strength = random.randint(10, 100)
    agility = random.randint(10, 100)
    intelligence = random.randint(10, 100)
    return Creature(name, ctype, element, strength, agility, intelligence)

def generate_creatures(n):
    return [generate_creature() for _ in range(n)]

def save_creatures(creatures, filename='creatures.json'):
    with open(filename, 'w') as f:
        json.dump([c.to_dict() for c in creatures], f, indent=2)

def load_creatures(filename='creatures.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [Creature(d['name'], d['type'], d['element'], d['strength'], d['agility'], d['intelligence']) for d in data]
    except FileNotFoundError:
        return []

def print_top_creatures(creatures, top_n=5):
    sorted_creatures = sorted(creatures, key=lambda c: c.power_level(), reverse=True)
    print(f"\nTop {top_n} Creatures by Power Level:")
    for c in sorted_creatures[:top_n]:
        print(f"{c} - Power Level: {c.power_level():.2f}")

def search_creatures(creatures, keyword):
    return [c for c in creatures if keyword.lower() in c.name.lower() or keyword.lower() in c.ctype.lower()]

def main_menu():
    creatures = load_creatures()
    while True:
        print("\n=== Fantasy Creature Generator ===")
        print("1. Generate new creatures")
        print("2. View top creatures")
        print("3. Search creatures")
        print("4. Save creatures")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            count = int(input("How many creatures to generate? "))
            new_creatures = generate_creatures(count)
            creatures.extend(new_creatures)
            print(f"{count} creatures generated.")
        elif choice == '2':
            print_top_creatures(creatures)
        elif choice == '3':
            keyword = input("Enter name or type to search: ")
            results = search_creatures(creatures, keyword)
            if results:
                for c in results:
                    print(c)
            else:
                print("No creatures found.")
        elif choice == '4':
            save_creatures(creatures)
            print("Creatures saved.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
