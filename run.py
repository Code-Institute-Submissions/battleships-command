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
        ships_placed = 0
        while ships_placed < self.num_ships:
            for i in range(self.num_ships):
                ships_placed += 1
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

    generate_boards(size, num_ships, name)


def generate_boards(size, num_ships, name):
    """
    Generates player and computer boards and updates each board with new
    values.
    """
    settings = GameArea(size, num_ships, name)
    board = settings.create_board()
    player_coordinates = settings.create_coordinates()
    computer_coordinates = settings.create_coordinates()

    print(" Computer's Board: ")
    print(computer_coordinates)
    print(*board, sep="\n")
    player_start = settings.ship_placements(board, player_coordinates)
    print(f"\n {name.capitalize()}'s Board: ")
    print(player_coordinates)
    print(*player_start, "\n", sep="\n")


new_game()
