# chohan_rb.py
"""Cho-Han, modified by Reed Bunnell
Original by Al Sweigart al@inventwithpython.com
Modified for CSD-325 Module 3 Assignment

Changes:
- Prompt uses 'rb:' instead of '>'
- House fee increased to 12%
- Bonus of 10 mon if dice total is 2 or 7
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, modified by Reed Bunnell

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

*** If the total of the dice is 2 or 7, you receive a 10 mon bonus! ***
''')

purse = 5000
while True:  # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('rb: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('rb: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    if total % 2 == 0:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if total == 2 or total == 7:
        print(f'Bonus! The dice total was {total}. You earn a 10 mon bonus.')
        purse += 10

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        houseFee = pot * 12 // 100
        print('The house collects a', houseFee, 'mon fee.')
        purse -= houseFee
    else:
        print('You lost!')
        purse -= pot

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
