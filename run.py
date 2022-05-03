class GameArea:
    """
    Constructs the game board, places battleships based on player input
    and receives player name input.
    """
    def __init__(self, size, num_ships, name, board_type):
        self.boardsize = size
        self.num_ships = num_ships
        self.name = name
        self.board_type = board_type
        self.comp_guess = []
        self.player_guess = []
        self.ships = []


def new_game():
    """
    Starts a new game instance. Sets player name, board size, number of ships
    based on inputs and prints input values.
    """
    name = input("Please enter your name: ")
    print(f"Welcome aboard {name}.\n")
    try:
        size = int(input("Select a board size between 5 & 10: "))
        print(f"You have chosen a board size of {size}\n")
    except ValueError:
        print("Please enter a number between 5 & 10.\n")
    try:
        num_ships = int(input("Choose a number of ships per player between"
                              " 1 & 10: "))
        print(f"You have chosen {num_ships} ships per player.\n")
    except ValueError:
        print("Please choose a number between 1 & 10.\n")


new_game()