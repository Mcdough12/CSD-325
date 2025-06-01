"""
Author: Reed Bunnell
Assignment: Module 1 - 100 Bottles of Beer Countdown
Description: This program asks the user how many bottles of beer are on the wall, then
uses a function to count down to 1, updating the lyrics along the way. Once finished,
the user is reminded to buy more beer.
"""

def countdown_beer(bottles):
    while bottles > 0:
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        else:
            next_bottles = bottles - 1
            bottle_word = "bottles" if next_bottles != 1 else "bottle"
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {next_bottles} {bottle_word} of beer on the wall.\n")
        bottles -= 1

def main():
    try:
        user_input = int(input("Enter number of bottles: "))
        if user_input < 1:
            print("Please enter a number greater than 0.")
        else:
            countdown_beer(user_input)
            print("Time to buy more beer!")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()
