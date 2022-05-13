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
            size = int(input("Select a board size between 5 and 10: "))
            if size not in range(5, 11):
                print("Number must be between 5 and 10.\n")
            else:
                print(f"You have chosen a board size of {size}\n")
                break
        except ValueError:
            print("Please enter a number between 5 and 10.\n")

    # sets number of ships based on user input
    while True:
        try:
            num_ships = int(input("Choose a number of ships per player between"
                                  " 1 and 10: "))
            if num_ships not in range(1, 11):
                print("Please choose a number between 1 and 10.\n")
            else:
                print(f"You have chosen {num_ships} ships per player.\n")
                break
        except ValueError:
            print("Please enter a number between 1 and 10.\n")

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


def generate_boards(name, computer_board, player_board, scores, guesses):
    """
    Generates player and computer boards with updated values.
    """
    print(" Computer's Board: ")
    print(*computer_board, sep="\n")
    print(f"\n {name.capitalize()}'s Board: ")
    print(*player_board, "\n", sep="\n")

    if len(guesses) > 0:
        print(f"{scores}You have already guessed:\n{guesses}\n")


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


def new_guess(size, guesses, player_type):
    """
    Takes input for new player guess or randomly generates new computer
    guess then calls confirm_hit with guess created
    """
    def player_guess(guesses):
        """
        Takes input for guess and repeats if guess is a duplicate
        """
        while True:
            try:
                x = int(input(f"Select a row between 1 and {size}: "))
                if x not in range(1, size + 1):
                    print(f"Please pick a number between 1 and {size}.")
                else:
                    break
            except ValueError:
                print(f"Please choose a number between 1 and {size}.")
        while True:
            try:
                y = int(input(f"Select a column between 1 and {size}: "))
                if y not in range(1, size + 1):
                    print(f"Please pick a number between 1 and {size}.")
                else:
                    break
            except ValueError:
                print(f"Please choose a number between 1 and {size}.")
        guess = x, y

        if guess in guesses:
            print(f"You have already guessed {guess}! Please pick again.")
            player_guess(guesses)
        else:
            print(f"You guessed: {guess}\n")
            return guess

    def computer_guess(guesses):
        """
        Generates guess with randint and repeats if guess is a duplicate
        """
        x = randint(1, size)
        y = randint(1, size)
        guess = x, y

        if guess in guesses:
            computer_guess(guesses)
        else:
            return guess

    if player_type == "player":
        guess = player_guess(guesses)
    else:
        guess = computer_guess(guesses)

    return guess


def new_round(settings, player_board, computer_board, 
              player_coordinates, computer_coordinates):
    """
    Stores game variables and continue_playing function, calls updates_scores,
    guesses_and_hits and new_guess functions.
    """
    # guess list variables
    player_guesses = []
    computer_guesses = []

    # hit list variables
    player_hits = []
    computer_hits = []

    # ships count and score variables
    player_ships = int(settings.num_ships)
    computer_ships = int(settings.num_ships)
    player_score = f"{settings.name}'s ships remaining: {player_ships}\n"
    computer_score = f"Computer's ships remaining: {computer_ships}\n"
    scores = player_score + computer_score

    def confirm_hit(coordinates, guess, player_type):
        """
        Checks if guess matches coordinates for player_type then appends
        guess and hit lists, updates player or computer score or
        returns nothing.
        """
        nonlocal player_hits
        nonlocal computer_hits
        nonlocal player_ships
        nonlocal computer_ships
        nonlocal player_guesses
        nonlocal computer_guesses

        for i, _ in enumerate(coordinates):
            if guess in coordinates[i]:
                if player_type == "player":
                    player_hits.append(guess)
                    computer_ships -= 1
                    print("You sunk a battleship!")
                else:
                    computer_hits.append(guess)
                    player_ships -= 1
                    print("The enemy sunk a battleship!")
            else:
                if player_type == "player":
                    player_guesses.append(guess)
                else:
                    computer_guesses.append(guess)
                return

    # skips continue_playing for first round
    if len(player_guesses) > 0:
        continue_playing()

    # prints board before first round input requested
    if len(player_guesses) == 0:
        generate_boards(settings.name, computer_board, player_board, scores,
                        player_guesses)

    # calls new_guess function for player and computer
    player_pick = new_guess(settings.size, player_guesses, "player")
    computer_pick = new_guess(settings.size, computer_guesses, "computer")

    # calls confirm_hit for player and computer
    confirm_hit(computer_coordinates, player_pick, "player")
    confirm_hit(player_coordinates, computer_pick, "computer")

    # updates computer and player boards then calls generate_boards
    computer_board = guesses_and_hits(computer_board, player_guesses,
                                      player_hits)
    player_board = guesses_and_hits(player_board, computer_guesses,
                                    computer_hits)
    generate_boards(settings.name, computer_board, player_board, scores,
                    player_guesses)


new_game()
