# Import necessary modules
from colorama import Back, Fore, init
import pyfiglet
import numpy as np
import sys
import math
import random
import string

# Initialize Colorama
init(autoreset=True)

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
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board, last_move_row=None, last_move_col=None, game_ongoing=True):
    """
    Print the game board with row and column labels.

    Parameters:
    - board: The game board to be printed.
    - last_move_row: The row of the last moved piece.
    - last_move_col: The column of the last moved piece.
    """
    col_labels = [str(i + 1) for i in range(COLUMN_COUNT)]
    row_labels = [string.ascii_lowercase[i] for i in range(ROW_COUNT)]

    # Find the maximum length of row labels to determine spacing
    max_row_label_length = max(len(label) for label in row_labels)

    # Print rows with row labels on the left side
    for i, row in enumerate(board):
        row_label = row_labels[i].ljust(max_row_label_length)
        print(f"{row_label} |", end="")
        
        for j, cell in enumerate(row):
            if game_ongoing and last_move_row is not None and last_move_col is not None and i == last_move_row and j == last_move_col:
                # Highlight the last moved cell with a different background color
                if cell == 1:
                    print(Back.YELLOW + f" {cell} ", end="")
                elif cell == 2:
                    print(Back.BLUE + f" {cell} ", end="")
            else:
                print(f" {cell} ", end="  ")
        print(Fore.RESET + "|")  # Reset color after printing each row

    # Print separator line
    print(' ' + '-----'.join([''] * (COLUMN_COUNT + 1)))

    # Print column labels beneath the rows
    col_label_line = ' ' + '    '.join(col_labels)
    print(col_label_line)
    print()

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
        print("Welcome to Connect 4!")
        print("1. Start Game")
        print("2. Exit")
        choice = int(input("Enter your choice: \n"))
        if choice == 1 :
            board = create_board()
            print_board(board)

            player_turn = 1

            while True:
                col = int(input(f"Player {player_turn}, choose a column (1:A to 7:G): ")) - 1
                row = get_next_open_row(board, col)
                piece = player_turn
                drop_piece(board, row, col, piece)

                print_board(board, last_move_row=row, last_move_col=col, game_ongoing=True)

                if winning_move(board, piece):
                    print(f"Player {piece} wins!!")
                    game_ongoing = False
                    break  # Exit the inner loop if there's a winner

                # Switch to the other player's turn
                player_turn = 3 - player_turn  # Alternates between 1 and 2

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing! Exiting...")
                break  # Exit the outer loop if players don't want to play again
        elif choice == "2":
            print("Exiting the game. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    T= 'CONNECT 4'
    art= pyfiglet.figlet_format(T, font="bulbhead")
    print(art)
    play_game()
