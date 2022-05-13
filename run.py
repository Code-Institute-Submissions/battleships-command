from random import randint


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
        board = [""] * self.size
        while i < self.size:
            board[i] = (" - " * self.size)
            i += 1
        return board

    def create_coordinates(self):
        """
        Create coordinates for each ship based on board size and num_ships
        chosen.
        """
        coordinates_created = 0
        ship_coordinates = []
        ship_coordinates.clear()
        while coordinates_created < self.num_ships:
            coordinates_created += 1
            x = randint(1, self.size)
            y = randint(1, self.size)
            coordinates = x, y
            ship_coordinates.append(coordinates)
        return ship_coordinates

    def ship_placements(self, board, coordinates):
        """
        Places ships on the board based on num_ships selected and board,
        coordinates arguements.
        """
        for i in range(self.num_ships):
            x, y = coordinates[i]
            board[x - 1] = board[x - 1][: (y - 1) * 3] + ' | ' + (
                board[x - 1][y * 3:])
        return board


def new_game():
    """
    Starts a new game instance. Sets player name, board size & number of ships
    based on inputs and prints input values.
    """
    name = input("Please enter your name: ")
    name = name.capitalize()
    print(f"Welcome aboard, commander {name}.\n")

    # sets board size based on user input
    while True:
        try:
            size = int(input("Select a board size between 5 & 10: "))
            if size not in range(6, 11):
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

    # creates variables from player input using GameArea class and methods
    settings = GameArea(size, num_ships, name)
    board = settings.create_board()
    player_coordinates = settings.create_coordinates()
    computer_coordinates = settings.create_coordinates()
    player_board = settings.ship_placements(board, player_coordinates)
    computer_board = settings.create_board()

    # calls new_round function with created variable values
    new_round(settings, player_board, computer_board,
              player_coordinates, computer_coordinates)


def update_board(board, guesses, hit_type):
    """
    Updates board with guess coordinates for each player.
    """
    for _, guess in enumerate(guesses):
        x, y = guess
        board[x - 1] = board[x - 1][: (y - 1) * 3] + f' {hit_type} ' + (
                board[x - 1][y * 3:])
    return board


def guesses_and_hits(board, guesses, hits):
    """
    Calls update_board with guesses and hits then returns updated board
    """
    update_board(board, guesses, "X")
    update_board(board, hits, "O")
    return board


def generate_boards(name, computer_board, player_board):
    """
    Generates player and computer boards with updated values.
    """
    print(" Computer's Board: ")
    print(*computer_board, sep="\n")
    print(f"\n {name.capitalize()}'s Board: ")
    print(*player_board, "\n", sep="\n")


def new_round(settings, player_board, computer_board, 
              player_coordinates, computer_coordinates):
    """
    Stores game variables continue_playing function, calls updates_scores,
    guesses_and_hits and new_guess functions.
    """
    # guess list variables
    player_guesses = []
    computer_guesses = []

    # hit list variables
    player_hits = []
    computer_hits = []

    # ship count and score variables
    player_ships = int(settings.num_ships)
    computer_ships = int(settings.num_ships)
    score = f"""{settings.name}'s Ships: {player_ships}
Computer's Ships: {computer_ships}"""

    # updates computer and player boards then prints to terminal
    computer_board = guesses_and_hits(computer_board, player_guesses,
                                      player_hits)
    player_board = guesses_and_hits(player_board, computer_guesses,
                                    computer_hits)
    generate_boards(settings.name, computer_board, player_board)

    def continue_playing():
        """
        Confirms if the player would like to continue playing based on input.
        """
        resume = input("Enter 'n' to quit or any other key to continue: ")
        while True:
            if resume == "n":
                print("Game over! \n")
                new_game()
            else:
                return

    # skips continue_playing for first round
    if len(player_guesses) > 0:
        continue_playing()


new_game()
