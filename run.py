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

def drop_piece(board, row, col, piece):
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

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

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

def winning_move(board, piece):
    """
    check for winning combination in horizontal, vertical and 
    negatively and positively sloped diagonals, respectively
    I f no winning combination is found then the function returns false.
    """
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ):
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ):
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True

    return False

                
def play_game():
    """
    Runs the game
    """
    while True:
        board = create_board()
        print_board(board)

        player_turn = 1

        while True:
            col = int(input(f"Player {player_turn}, choose a column (1:A to 7:G): ")) - 1
            row = get_next_open_row(board, col)
            piece = player_turn
            drop_piece(board, row, col, piece)

            print_board(board)

            if winning_move(board, piece):
                print(f"Player {piece} wins!!")
                break  # Exit the inner loop if there's a winner

            # Switch to the other player's turn
            player_turn = 3 - player_turn  # Alternates between 1 and 2

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Exiting...")
            break  # Exit the outer loop if players don't want to play again

if __name__ == "__main__":
    print("Welcome to Connect 4!")
    play_game()
