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
   
    for r in range(ROW_COUNT - 1, -1, -1):
            if board[r][col] == 0:
                board[r][col] = piece
                break
            
def is_valid_location(board, col):
     """
     Function to check if any cell in a specified column has a value of 0.
     It checks each row in the specified column to see if any cell has a value of 0.
     If it finds at least one zero, the column is considered valid for placing a piece.
     """
     return any(board[r][col] == 0 for r in range(ROW_COUNT))

def get_next_open_row(board, col):
    """
    Get the index of the next available (empty) row in the specified column.

    Parameters:
    - board: The game board represented as a 2D NumPy array.
    - col: The column for which to find the next available row.

    Returns:
    The index of the next available row in the specified column, or None if the
    column is already full.
    """
    for r in range(ROW_COUNT - 1, -1, -1):
        if board[r][col] == 0:
            return r


def get_valid_columns(board):
    """
    Get a list of valid column indices where a player can make a move.
    """
    valid_columns = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_columns.append(col)
    return valid_columns

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
    #column_spacing = 3
    # Initialize background colors
    player_backgrounds = [Back.YELLOW, Back.BLUE]

    # Print rows with row labels on the left side
    for i, row in enumerate(board):
        row_label = row_labels[i].ljust(max_row_label_length)
        print(f"{row_label} |", end=" ")

        for j, cell in enumerate(row):
            if game_ongoing and last_move_row is not None and last_move_col is not None and i == last_move_row and j == last_move_col:
                # Highlight the last moved cell with a different background color
                player_index = cell - 1  # Player 1 has index 0, Player 2 has index 1
                print(f"{player_backgrounds[player_index]}{Fore.RESET} {cell} {Fore.RESET}", end="")
            else:
                player_index = cell - 1 if cell in [1, 2] else None
                background_color = player_backgrounds[player_index] if player_index is not None else ''
                print(f"{background_color} {cell} {Fore.RESET}", end=" ")

        print(Fore.RESET + "|")  # Reset color after printing each row

    # Print separator line
    print('   ' + '----'.join([''] * (COLUMN_COUNT + 1)))

    # Print column labels beneath the rows
    col_label_line = ' ' + '   '.join(col_labels)
    print(" "+col_label_line)
    print()

def winning_move(board, piece):
    """
    Check for a winning combination in horizontal, vertical, and 
    negatively and positively sloped diagonals, respectively.
    If no winning combination is found, then the function returns false.
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

def score_window(window, piece):
    """
    This function evaluates a window of positions in the game.
    It calculates a score for a given "window" in a Connect Four game
    to evaluate the strength of a particular configuration of four adjacent 
    positions in the game grid.

    Notably, the scores are arbitrary and used simply to quantify the strengths of the four configurations.
    """
    
    score = 0
    opponent_piece = 1 if piece == 2 else 2
    # Check if all positions contain a player's piece and add 100 to the score
    if window.count(piece) == 4:
        score += 100
    # Check if there are three occurrences of a player's piece and one empty. A potential win gets 5
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    # Check if there are two occurrences and two empty. Less likely to win. Add 2 to the score
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2
    # If there are three occurrences of the opponent's piece and one empty position (0), subtract 4 from the score
    if window.count(opponent_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score

def evaluate_game_state(board, piece):
    score = 0

    # Evaluate the center column
    center_list = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
    center_list_count = center_list.count(piece)
    score += center_list_count * 3

    # Evaluate rows, columns, and diagonals
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            # Evaluate rows
            if c <= COLUMN_COUNT - 4:
                row_window = [int(board[r][c + i]) for i in range(4)]
                score += score_window(row_window, piece)

            # Evaluate columns
            if r <= ROW_COUNT - 4:
                col_window = [int(board[r + i][c]) for i in range(4)]
                score += score_window(col_window, piece)

            # Evaluate diagonals
            if c <= COLUMN_COUNT - 4 and r <= ROW_COUNT - 4:
                diagonal_up_window = [int(board[r + i][c + i]) for i in range(4)]
                score += score_window(diagonal_up_window, piece)

            if c <= COLUMN_COUNT - 4 and r >= 3:
                diagonal_down_window = [int(board[r - i][c + i]) for i in range(4)]
                score += score_window(diagonal_down_window, piece)

    return score

def is_game_over(board):
    """
    Check if the game is over by either a player winning or the board being full.
    """
    return winning_move(board, 1) or winning_move(board, 2) or len(get_valid_columns(board)) == 0

def play_game():
    # Run the game
    while True:
        print("Welcome to Connect 4!")
        print("1. Start Game")
        print("2. Exit")
        choice = int(input("Enter your choice: \t"))

        if choice == 1:
            board = create_board()
            print_board(board)

            player_turn = 1
            game_ongoing = True

            while game_ongoing:
                valid_columns = get_valid_columns(board)

                while True:
                    try:
                        col = int(input(f"Player {player_turn}, choose a column (1 - 7), or enter 0 to exit: ")) - 1
                        if col == -1:
                            print("Exiting the game. Goodbye!")
                            sys.exit()
                        elif col in valid_columns:
                            break
                        else:
                            print("Invalid choice. Please choose a valid column.")
                    except ValueError:
                            print('Invalid choice- must be value 1-7')


                row = get_next_open_row(board, col)
                piece = player_turn
                drop_piece(board, row, col, piece)

                print_board(board, last_move_row=row, last_move_col=col, game_ongoing=True)

                if winning_move(board, piece):
                    print(f"Player {piece} wins!!")
                    game_ongoing = False
                    break  # Exit the inner loop if there's a winner

                if is_game_over(board):
                    print("It's a tie!")
                    game_ongoing = False
                    break

                # Evaluate the current board state
                current_score = evaluate_game_state(board, piece)
                print(f"Score for Player {piece}: {current_score}")

                # Switch to the other player's turn
                player_turn = 3 - player_turn  # Alternates between 1 and 2

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing! Exiting...")
                game_ongoing = False  # Exit the inner loop if players don't want to play again
                break

        elif choice == 2:
            print("Exiting the game. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    T = 'CONNECT 4'
    art = pyfiglet.figlet_format(T, font="bulbhead")
    print(art)
    play_game()
