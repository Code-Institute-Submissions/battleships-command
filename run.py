from random import randint
# import keyboard

score = {"Player Ships": 0, "Computer Ships": 0}


class GameArea:
    """
    Class container that constructs the game board, generates ship coordinates
    based on player input and receives player name input.
    """
    def __init__(self, size, num_ships, name):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.player_guesses = []
        self.computer_guesses = []

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

    settings = GameArea(size, num_ships, name)
    board = settings.create_board()
    player_coordinates = settings.create_coordinates()
    computer_coordinates = settings.create_coordinates()

    new_round(settings, board, player_coordinates, computer_coordinates)


def generate_boards(name, computer_board, player_board, player_guesses,
                    computer_guesses):
    """
    Generates player and computer boards and updates each board with new
    values.
    """
    def update_board(board, guesses):
        """
        Updates board with guess coordinates for each player
        """
        for i in range(len(guesses)):
            x, y = guesses[i]
            board[x - 1] = board[x - 1][: (y - 1) * 3] + ' X ' + (
                    board[x - 1][y * 3:])
        return board

    computer_board = update_board(computer_board, player_guesses)
    player_board = update_board(player_board, computer_guesses)

    print(" Computer's Board: ")
    print(*computer_board, sep="\n")
    print(f"\n {name.capitalize()}'s Board: ")
    print(*player_board, "\n", sep="\n")


def new_round(settings, board, player_coordinates, computer_coordinates):
    """
    Confirms if player would like to continue playing, updates scores, boards
    player guesses, computer guesses and receives input for player guess.
    """
    player_board = settings.ship_placements(board, player_coordinates)
    computer_board = settings.create_board()
    player_guesses = [(1, 3), (4, 6)]
    computer_guesses = [(1, 3), (5, 7), (9, 5)]
    player_ships = settings.num_ships
    computer_ships = settings.num_ships

    # def continue_playing():
    #     """
    #     Confirms if the player would like to continue playing based on input
    #     """
    #     input("Press 'n' to stop playing or any other key to continue \n")
    #     while True:
    #         if keyboard.read_key() == "n":
    #             print("Game over! \n")
    #         else:
    #             return

    # # skips continue_playing for first round
    # if len(player_guesses) > 0:
    #     continue_playing()

    generate_boards(settings.name, computer_board, player_board,
                    player_guesses, computer_guesses)


new_game()
