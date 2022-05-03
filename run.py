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
