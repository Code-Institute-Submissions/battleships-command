from random import randint


class GameArea:
    """
    Class container that onstructs the game board, places battleships based
    on player input and receives player name input.
    """
    def __init__(self, size, num_ships, name):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.comp_guess = []
        self.player_guess = []
        self.ships = []

    def create_board(self, size):
        """
        Creates board for each player based on size input
        """
        board = []
        i = 0
        while i < size:
            board.append(" - " * size)
            i += 1
        return board


def new_game():
    """
    Starts a new game instance. Sets player name, board size & number of ships
    based on inputs and prints input values.
    """
    name = input("Please enter your name: ")
    print(f"Welcome aboard, commander {name}.\n")

    # sets board size based on user input
    while True:
        try:
            size = int(input("Select a board size between 5 & 10: "))
            if size not in range(5, 10):
                print("Number must be between 5 & 10.\n")
            else:
                print(f"You have chosen a board size of {size}\n")
                break
        except ValueError:
            print("Please enter a number between 5 & 10.\n")

    # sets number of ships based on user input
    while True:
        try:
            num_ships = int(input("Choose a number of ships per player between"
                                  " 1 & 10: "))
            if num_ships not in range(1, 10):
                print("Please choose a number between 1 & 10.\n")
            else:
                print(f"You have chosen {num_ships} ships per player.\n")
                break
        except ValueError:
            print("Please enter a number between 1 & 10.\n")

    GameArea(size, num_ships, name)


new_game()
