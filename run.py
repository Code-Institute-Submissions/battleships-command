from random import randint

score = {"Player Score": 0, "Computer Score": 0}


class GameArea:
    """
    Class container that constructs the game board, generates ship coordinates
    based on player input and receives player name input.
    """
    def __init__(self, size, num_ships, name):
        self.size = size
        self.num_ships = num_ships
        self.name = name

    def create_board(self):
        """
        Creates board for each player based on size input
        """
        i = 0
        board = ""
        while i < self.size:
            i += 1
            board += (" - " * self.size + "\n")
        return board

    def create_coordinates(self):
        """
        Create coordinates for each ship based on board size and num_ships
        chosen.
        """
        ships_placed = 0
        ship_placements = []
        while ships_placed < self.num_ships:
            ships_placed += 1
            x = randint(1, self.size)
            y = randint(1, self.size)
            coordinates = {x: y}
            ship_placements.append(coordinates)
        return ship_placements


class Player(GameArea):
    """
    Subclass for player guesses and ship coordinates.
    """
    def __init__(self, player_guess, player_ships):
        self.player_guess = player_guess
        self.player_ships = player_ships


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
            if size not in range(5, 11):
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
            if num_ships not in range(1, 11):
                print("Please choose a number between 1 & 10.\n")
            else:
                print(f"You have chosen {num_ships} ships per player.\n")
                break
        except ValueError:
            print("Please enter a number between 1 & 10.\n")

    settings = GameArea(size, num_ships, name)
    computer_board = f"Computer's Board: \n{settings.create_board()}"
    player_board = f"Player's Board: \n{settings.create_board()}"
    print(computer_board, player_board)


new_game()
