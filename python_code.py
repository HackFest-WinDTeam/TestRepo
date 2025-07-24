import random
import os
import time

# Define a list of characters and ANSI color codes
chars = ['@', '#', '$', '%', '&', '*', '+', '=', '-', ':', ';']
colors = [31, 32, 33, 34, 35, 36, 37]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_art(width=80, height=25):
    for _ in range(height):
        line = ''
        for _ in range(width):
            char = random.choice(chars)
            color = random.choice(colors)
            line += f"\033[{color}m{char}\033[0m"
        print(line)

if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            generate_art()
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nArt session ended.")
