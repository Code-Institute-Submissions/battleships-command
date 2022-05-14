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
        self.player_hits = []
        self.computer_hits = []
        self.player_ships = num_ships
        self.computer_ships = num_ships
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

    def confirm_hit(self, coordinates, guess, player_type):
        """
        Checks if guess matches coordinates for player_type then appends
        guess and hit lists, updates player or computer score or
        returns nothing.
        """
        for i, _ in enumerate(coordinates):
            if guess in coordinates[i]:
                if player_type == "player":
                    self.player_hits.append(guess)
                    self.computer_ships -= 1
                    print("You sunk a battleship!")
                else:
                    self.computer_hits.append(guess)
                    self.player_ships -= 1
                    print("The enemy sunk a battleship!")
            else:
                if player_type == "player":
                    self.player_guesses.append(guess)
                else:
                    self.computer_guesses.append(guess)
                return


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
    Prints player and computer boards with updated values.
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
        pick = x, y

        if pick in guesses:
            print(f"You have already guessed {pick}! Please pick again.")
            player_guess(guesses)
        else:
            print(f"You guessed: {pick}\n")
            guess = pick
            return guess

    def computer_guess(guesses):
        """
        Generates guess with randint and repeats if guess is a duplicate
        """
        x = randint(1, size)
        y = randint(1, size)
        pick = x, y

        if pick in guesses:
            computer_guess(guesses)
        else:
            guess = pick
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
    p_score = f"{settings.name}'s ships remaining: {settings.player_ships}\n"
    c_score = f"Computer's ships remaining: {settings.computer_ships}\n"
    scores = p_score + c_score

    # skips continue_playing for first round
    if len(settings.player_guesses) > 0:
        continue_playing()

    # prints board before first round input requested
    if len(settings.player_guesses) == 0:
        generate_boards(settings.name, computer_board, player_board, scores,
                        settings.player_guesses)

    # calls new_guess function for player and computer
    player_pick = new_guess(settings.size, settings.player_guesses, "player")
    computer_pick = new_guess(settings.size, settings.computer_guesses,
                              "computer")

    # calls confirm_hit for player and computer
    settings.confirm_hit(computer_coordinates, player_pick, "player")
    settings.confirm_hit(player_coordinates, computer_pick, "computer")

    # updates computer and player boards then calls generate_boards
    computer_board = guesses_and_hits(computer_board, settings.player_guesses,
                                      settings.player_hits)
    player_board = guesses_and_hits(player_board, settings.computer_guesses,
                                    settings.computer_hits)
    generate_boards(settings.name, computer_board, player_board, scores,
                    settings.player_guesses)

    # starts new_round function with updated data
    new_round(settings, player_board, computer_board,
              player_coordinates, computer_coordinates)


new_game()
