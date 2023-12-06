class Game:
    """Game object"""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.current_player = self.player1
        self.opponent_player = self.player2

