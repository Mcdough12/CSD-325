"""Forest Fire Sim, modified by Reed Bunnell for CSD-325 Assignment 6.2
A simulation of wildfires spreading in a forest with a central lake acting as a firebreak.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # New character for the lake

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5

# Define lake boundaries (center area)
LAKE_X_START = WIDTH // 3
LAKE_X_END = WIDTH * 2 // 3
LAKE_Y_START = HEIGHT // 3
LAKE_Y_END = HEIGHT * 2 // 3

def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue

                current = forest[(x, y)]

                if current == WATER:
                    nextForest[(x, y)] = WATER  # Water remains unchanged
                elif current == EMPTY and random.random() <= GROW_CHANCE:
                    nextForest[(x, y)] = TREE
                elif current == TREE and random.random() <= FIRE_CHANCE:
                    nextForest[(x, y)] = FIRE
                elif current == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            if forest.get(neighbor) == TREE:
                                nextForest[neighbor] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = current

        forest = nextForest
        time.sleep(PAUSE_LENGTH)

def createNewForest():
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if LAKE_X_START <= x <= LAKE_X_END and LAKE_Y_START <= y <= LAKE_Y_END:
                forest[(x, y)] = WATER  # Add lake in the center
            elif random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest

def displayForest(forest):
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg('blue')
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
