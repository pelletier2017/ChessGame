from game import ChessGame


class ChessTournament:
    def __init__(self, player1, player2, num_games, verbosity=1):
        self._player1 = player1
        self._player2 = player2
        self._num_games = num_games
        self._verbosity = verbosity

    def play_games(self):
        p1_score = 0
        p2_score = 0
        for i in range(self._num_games):
            game = ChessGame(self._player1, self._player2,
                             verbosity=self._verbosity, pause=0)
            result = game.play()
            if result["winner"] is self._player1:
                p1_score += 1
            elif result["winner"] is self._player2:
                p2_score += 1
        return "Player1 score: {}, Player2 score: {}".format(p1_score, p2_score)