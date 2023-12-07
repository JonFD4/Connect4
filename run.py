# Import necessary modules
import numpy as np
import sys
import math
import random
import string

# Define constants
ROW_COUNT, COLUMN_COUNT = 6, 7

def create_board():
    """
    Create a 2D NumPY list matrix with dimensions specified by 
    ROW_COUNT and COLUMN_COUNT.
    The array is initialized with zeros, and dtype=int 
    ensures that the elements of the array are of integer data type.
    """
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

def drop_piece(board, col, piece):
    '''
    Update the game board by placing the specified game piece in the lowest
    available row of the specified column. The function modifies the game
    board in-place.

    Parameters:
    - board: The game board to be updated.
    - col: The column where the piece will be placed.
    - piece: The game piece to be placed ('A' or '0').
    '''
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = piece
            break

def print_board(board):
    """
    Print the game board with row and column labels.

    Parameters:
    - board: The game board to be printed.
    """
    col_labels = [chr(ord('A') + i) for i in range(COLUMN_COUNT)]
    row_labels = [string.ascii_lowercase[i] for i in range(ROW_COUNT)]

    # Print column labels
    print('  ' + ' '.join(col_labels))

    # Print rows with row labels
    for i, row in enumerate(board):
        row_str = ' '.join(map(str, row))
        print(f"{row_labels[i]} {row_str}")

def play_game():
    """
    Runs the game
    """
    board = create_board()

    drop_piece(board, 2, 1)
    drop_piece(board, 2, 2)
    drop_piece(board, 3, 1)
    drop_piece(board, 3, 2)

    print_board(board)

play_game()
