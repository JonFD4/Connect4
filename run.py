# Import necessary modules
from colorama import Back, Fore, init
import pyfiglet
import numpy as np
import sys
import string
import time
import textwrap

# Initialize Colorama
init(autoreset=True)

# Define constants
ROW_COUNT, COLUMN_COUNT = 6, 7

# Define and formatting rules
width = 50
PERSON_RULES = """This game is played on a vertical grid with 6 rows and 7 columns.
Two players take turns placing their colored discs (player 1:yellow/1 and player 2: blue/2) into any column of their choice.
The piece will fall to the lowest available position within the chosen column.
The objective is to be the first to connect four of your own colored discs in a row, either horizontally, vertically, or diagonally.
Once a player has achieved a connect four, they win the game!
If all the columns are filled without a connect four, the game ends in a draw."""

COMPUTER_RULES = """This game is played on a vertical grid with 6 rows and 7 columns.
You and computer take turns placing your colored discs (player 1:yellow/1 and computer: blue/2) into any column of your choice.
The piece will fall to the lowest available position within the chosen column.
The objective is to be the first to connect four of your own colored discs in a row, either horizontally, vertically, or diagonally.
Once you or the computer has achieved a connect four, either one of you is the winner!
If all the columns are filled without a connect four, the game ends in a draw. """


def format_text_line(text, width):
    """
   This function loops through text and turns into a numbered list based on the number of lines
    """
    lines = text.split("\n")

    numbered_lines = ""
    for i, line in enumerate(lines, start=1):
        listed_lines = textwrap.fill(line, width)
        numbered_lines += f"{i}. {listed_lines} \n \n"
    return numbered_lines.strip()


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


def print_board(board, last_move_row=None,
                last_move_col=None, game_ongoing=True):
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

    # Initialize background colors
    player_backgrounds = [Back.YELLOW, Back.BLUE]

    # Print rows with row labels on the left side
    for i, row in enumerate(board):
        row_label = row_labels[i].ljust(max_row_label_length)
        print(f"{row_label} |", end=" ")

        for j, cell in enumerate(row):
            if game_ongoing and last_move_row is not None and last_move_col is not None and i == last_move_row and j == last_move_col:
                # Highlight the last moved cell with a different background
                # color
                player_index = cell - 1  # Player 1 has index 0, Player 2 has index 1
                print(
                    f"{player_backgrounds[player_index]}{Fore.RESET} {cell} {Fore.RESET}",
                    end=" ")
            else:
                player_index = cell - 1 if cell in [1, 2] else None
                background_color = player_backgrounds[player_index] if player_index is not None else ''
                print(f"{background_color} {cell} {Fore.RESET}", end=" ")

        print(Fore.RESET + " |")  # Reset color after printing each row

    # Print separator line
    print('   ' + '----'.join([''] * (COLUMN_COUNT + 1)))

    # Print column labels beneath the rows
    col_label_line = '  ' + '   '.join(col_labels)
    print("  " + " " + col_label_line)
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
    # Check if there are three occurrences of a player's piece and one empty.
    # A potential win gets 5
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    # Check if there are two occurrences and two empty. Less likely to win.
    # Add 2 to the score
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2
    # If there are three occurrences of the opponent's piece and one empty
    # position (0), subtract 4 from the score
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
                diagonal_up_window = [int(board[r + i][c + i])
                                      for i in range(4)]
                score += score_window(diagonal_up_window, piece)

            if c <= COLUMN_COUNT - 4 and r >= 3:
                diagonal_down_window = [
                    int(board[r - i][c + i]) for i in range(4)]
                score += score_window(diagonal_down_window, piece)

    return score


def is_game_over(board):
    """
    Check if the game is over by either a player winning or the board being full.
    """
    return winning_move(board, 1) or winning_move(
        board, 2) or len(get_valid_columns(board)) == 0


def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or is_game_over(board):
        # Assuming the computer is always the maximizing player
        return evaluate_game_state(board, 2)

    valid_columns = get_valid_columns(board)

    if maximizing_player:
        max_eval = float('-inf')
        for col in valid_columns:
            row = get_next_open_row(board, col)
            temp_board = np.copy(board)
            # Assuming the computer is player 2
            drop_piece(temp_board, row, col, 2)
            eval = minimax(temp_board, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for col in valid_columns:
            row = get_next_open_row(board, col)
            temp_board = np.copy(board)
            # Assuming the human player is player 1
            drop_piece(temp_board, row, col, 1)
            eval = minimax(temp_board, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_computer_move(board):
    """
    Generate a random valid move for the computer player.
    """
    valid_columns = get_valid_columns(board)
    best_score = float('-inf')
    best_move = None

    for col in valid_columns:
        row = get_next_open_row(board, col)
        temp_board = np.copy(board)
        # Assuming the computer is player 2
        drop_piece(temp_board, row, col, 2)
        score = minimax(temp_board, 4, False, float('-inf'),
                        float('inf'))  # Adjust the depth as needed
        if score > best_score:
            best_score = score
            best_move = col

    return best_move


def play_against_computer():
    board = create_board()
    print(format_text_line(COMPUTER_RULES, width) + "\n ")
    print("You are playing against the Computer (Player 2)\n")
    print_board(board)

    player_turn = 1
    game_ongoing = True

    while game_ongoing:
        valid_columns = get_valid_columns(board)

        while True:
            try:
                if player_turn == 1:
                    col = int(
                        input(f"Player {player_turn}, choose a column (1 - 7), or enter 0 to exit: ")) - 1
                    if col == -1:
                        print("Exiting the game. Goodbye!")
                        sys.exit()
                else:
                    # Computer's turn
                    print("Computer is thinking...")
                    # Introduce a delay to make the computer's move more
                    # visible
                    time.sleep(1)
                    col = get_computer_move(board)
                    print(f"Computer chooses column {col + 1} \n")

                if col in valid_columns:
                    break
                else:
                    print("Invalid choice. Please choose a valid column.")
            except ValueError:
                print('Invalid choice- must be value 1-7')

        row = get_next_open_row(board, col)
        piece = player_turn
        drop_piece(board, row, col, piece)

        print_board(
            board,
            last_move_row=row,
            last_move_col=col,
            game_ongoing=True)

        if winning_move(board, piece):
            if player_turn == 1:
                print(f"Player {piece} wins!!")
            else:
                print("Computer wins!")
            game_ongoing = False
            break  # Exit the inner loop if there's a winner

        if is_game_over(board):
            print("It's a tie!")
            game_ongoing = False
            break

        # Evaluate the current board state
        current_score = evaluate_game_state(board, piece)
        print(f"Player {piece} dropped a piece in column {col + 1}")
        print(f"Score for Player {piece}: {current_score }\n")

        # Switch to the other player's turn
        player_turn = 3 - player_turn  # Alternates between 1 and 2

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'")
            play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again == 'no':
            print("Thanks for playing! Exiting...")
            sys.exit()
            break  # Exit the outer loop if players don't want to play again

        else:
            print(art)
            play_game()


def play_game():
    # Run the game
    while True:
        print("Welcome to Connect 4! \n")
        print("1. Play with Friend")
        print("2. Play against Computer")
        print("3. Exit \n")
        try:
            choice = int(input("Enter your choice: \n"))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if choice == 1:
            board = create_board()
            print("You will be playing against your friend\n")
            print(format_text_line(PERSON_RULES, width) + "\n ")
            print_board(board)

            player_turn = 1
            game_ongoing = True

            while game_ongoing:
                valid_columns = get_valid_columns(board)

                while True:
                    try:
                        col = int(
                            input(f"Player {player_turn}, choose a column (1 - 7), or enter 0 to exit: ")) - 1
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

                print_board(
                    board,
                    last_move_row=row,
                    last_move_col=col,
                    game_ongoing=True)

                if winning_move(board, piece):
                    print(f"Player {piece} wins!!\n")
                    game_ongoing = False
                    break  # Exit the inner loop if there's a winner

                if is_game_over(board):
                    print("It's a tie! \n")
                    game_ongoing = False
                    break

                # Evaluate the current board state
                current_score = evaluate_game_state(board, piece)
                print(f"Player {piece} dropped a piece in column {col + 1}")
                print(f"Score for Player {piece}: {current_score} \n")

                # Switch to the other player's turn
                player_turn = 3 - player_turn  # Alternates between 1 and 2
            while True:
                play_again = input(
                    "Do you want to play again? (yes/no): ").lower()
                while play_again not in ['yes', 'no']:
                    print("Invalid input. Please enter 'yes' or 'no'")
                    play_again = input(
                        "Do you want to play again? (yes/no): ").lower()

                if play_again == 'no':
                    print("Thanks for playing! Exiting...")
                    sys.exit()
                    break  # Exit the outer loop if players don't want to play again

                else:
                    print(art)
                    play_game()

        elif choice == 2:
            play_against_computer()
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    T = 'CONNECT 4'
    art = pyfiglet.figlet_format(T, font="bulbhead")
    print(art)
    play_game()
