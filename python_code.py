import random
import os
import time
import argparse

# Define a list of characters and ANSI color codes
chars = ['@', '#', '$', '%', '&', '*', '+', '=', '-', ':', ';']
colors = [31, 32, 33, 34, 35, 36, 37, 90, 91, 92]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_art(width=80, height=25, frame=0):
    lines = [f"\033[1mFrame: {frame}\033[0m\n"]
    for _ in range(height):
        line = ''.join(
            f"\033[{random.choice(colors)}m{random.choice(chars)}\033[0m"
            for _ in range(width)
        )
        lines.append(line)
    print('\n'.join(lines))

def random_bg_flash():
    bg_color = random.randint(40, 47)
    print(f"\033[{bg_color}m", end='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASCII Art Generator")
    parser.add_argument('--width', type=int, default=80, help='Width of the art')
    parser.add_argument('--height', type=int, default=25, help='Height of the art')
    args = parser.parse_args()

    frame_count = 0
    try:
        while True:
            clear_screen()
            if random.random() < 0.1:
                random_bg_flash()
            generate_art(width=args.width, height=args.height, frame=frame_count)
            frame_count += 1
            time.sleep(0.15)
    except KeyboardInterrupt:
        print(f"\n\033[93mArt session ended after {frame_count} frames. Goodbye!\033[0m")

#Rev by Marek Matyja 