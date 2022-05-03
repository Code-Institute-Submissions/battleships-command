class GameArea:
    """
    Constructs the game board, places battleships based on player input
    and receives player name input.
    """
    playername = input("Please enter your name: ")
    print(f"Welcome aboard {playername}")
    boardsize = int(input("Choose a board size between 5 & 10: "))
    print(f"You have chosen a board size of {boardsize}")

    def __init__(self, playername, boardsize):
        self.playername = playername
        self.boardsize = boardsize

    def board_setup(self):
        """
        Creates the board for player and computer based on board size
        input
        """
        board = ""
        for n in range(self.boardsize):
            board_row = print(" - " * self.boardsize)
            board_row.append(board)

        return board

    board_setup()