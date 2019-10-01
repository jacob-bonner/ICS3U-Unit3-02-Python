#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This is a rudimentary "guess the number" program


import constants


def main():
    # This function allows the user to try and guess the number

    # Input
    user_guess = int(input("Guess the number between 1 & 9 (integer): "))
    print("")

    # process
    if user_guess == constants.CORRECT_NUMBER:
        # Output 1
        print("You correctly guessed the number!")


if __name__ == "__main__":
    main()
