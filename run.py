# Import necessary modules
import numpy as np
import sys
import math
import random

# Define constants
ROW_COUNT, COLUMN_COUNT = 6, 7


def create_board():
    """
    Create a 2d NumPY list matrix with dimensions specified by 
    ROW_COUNT and COLUMN_COUNT.
    The array is initialized with zeros, and dtype=int 
    ensures that the elements of the array are of integer data type.
    """
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

def print_board(board):
    """
    Iterate over each row in the 2D list board.
    Convert each element in the current row to string.
    The space created using .join represents row as a space-spearated string.
    Print all rows on a single line without square brackets.

    """
    for row in board:
        print(' '.join(map(str, row)), end= '')
    print()

def play_game():
    """
    Runs the game
    """
    board = create_board()
    print(board)
play_game()