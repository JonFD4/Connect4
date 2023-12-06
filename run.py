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


def drop_piece(board, row, col, piece):
    '''
    the function updates the game board (board) by placing 
    the specified game piece (piece) in the specified row (row) and column (col). 
    It modifies the game board in-place.
    '''
    board[row][col] = piece

def print_board(board):
    """
    Iterate over each row in the 2D list board.
    Convert each element in the current row to string.
    The space created using .join represents row as a space-spearated string.
    Print all rows on a single line without square brackets.

    """
    for row in board:
        print(' '.join(map(str, row)))
    print()

def play_game():
    """
    Runs the game
    """
    board = create_board()

    drop_piece(board, 0, 2, 1)
    print_board(board)
play_game()