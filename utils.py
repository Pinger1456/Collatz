"""Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart al@inventwithpython.com
"""
import sys


def get_starting_number():
    """Prompt the user for a valid starting number for the Collatz sequence."""
    response = input('Enter a starting number (greater than 0) or QUIT:\n> ')
    try:
        n = int(response)
        if n <= 0:
            raise ValueError
        return n
    except ValueError:
        print('You must enter an integer greater than 0.')
        sys.exit()
