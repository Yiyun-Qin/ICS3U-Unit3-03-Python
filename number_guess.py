#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on March 2022
# This is the math program, comparing the guessed number and answer

import constants


def main():
    # This function calculates the number guess game
    # The game compares the guessed number and the answer

    # input
    number_guess = int(input("Enter the number you guess between 0 - 9: "))

    # process
    if number_guess == constants.ANSWER:
        # output
        print("")
        print("Your guess is right!")
    if number_guess != constants.ANSWER:
        # output
        print("")
        print("Your guess is wrong!")


if __name__ == "__main__":
    main()
