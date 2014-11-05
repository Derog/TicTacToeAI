__author__ = 'derog'

import fileinput


class Board():
    def __init__(self):
        # 0 empty, 1 first player, -1 second player
        self._board_values = [[0 for j in range(3)] for i in range(3)]
        self._is_game_not_ended = True
        self._number_of_moves = 0
        self.winner = 0

    def is_game_notended(self):
        return self._is_game_not_ended

    def move(self, xposition, yposition, value):
        if xposition is None or yposition is None:
            raise ValueError("Didnt receive a valid position")

        if self._board_values[xposition][yposition] == 0:
            self._board_values[xposition][yposition] = value
            self._number_of_moves += 1
        else:
            raise IndexError("Tryng to insert in an occupied position")

            # TODO <Detection of game ending>

    def number_of_moves(self):
        return self._number_of_moves

    def __call__(self, *args, **kwargs):
        self.move(args[0][0], args[0][1], args[1])

    def __str__(self):
        text = '#=#=#=#'

        for i in range(3):
            text += '\n'
            text += '|'
            for j in range(3):
                if self._board_values[i][j] == 0:
                    text += ' '
                elif self._board_values[i][j] == 1:
                    text += 'X'
                elif self._board_values[i][j] == -1:
                    text += 'O'
                text += '|'
            text += '\n#=#=#=#'

        return text

    def getBoardValues(self):
        return self._board_values

    def __bool__(self):
        return self.is_game_notended()

    def __len__(self):
        return self._numeber_of_moves

    def winner(self):
        return self.winner


class Player():
    def __init__(self, name, brain=None, human=False):
        self.name = name
        self._is_human = human
        if brain is not None:
            self.brain = brain

    def is_human(self):
        return self._is_human

    def has_brain(self):
        if self.is_human():
            print("Humans don't need brains")
            return False
        else:
            if self.brain is not None:
                return True
            else:
                return False

    def getName(self):
        return self.name

    def move(self, board, lastmove):
        if self.is_human():
            move = []
            move[0] = fileinput.input()
            move[1] = fileinput.input()
            return move
        else:
            if self.has_brain():
                return self.brain(board, lastmove)
            else:
                print("If the player is not an human a brain needs to be loaded")
                return None

    def LoadBrain(self, brain):
        self.brain = brain

    def __str__(self):
        return self.getName()


class Game():
    def __init__(self, player1, player2, turn=1):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.turn = turn
        self._winner = None
        self.lastmove = (None, None)

    def move(self):
        if self.turn == 1:
            self.lastmove = self.player1.move(self.board.getBoardValues(), self.lastmove)
        else:
            self.lastmove = self.player2.move(self.board.getBoardValues(), self.lastmove)
        self.board.move(self.lastmove[0], self.lastmove[1], self.turn)
        self.turn *= -1

        if not self.board.is_game_notended():
            self.winner = self.board.winner()


    def __bool__(self):
        return self.board.is_game_notended()

    def __str__(self):
        text = 'Player1 is ' + self.player1.getName() + '\n'
        text += 'Player2 is ' + self.player2.getName() + '\n'
        text += str(self.board)
        return text

    def __iter__(self):
        self.move()

    def is_game_ended(self):
        pass

    def number_of_moves(self):
        return self.board.number_of_moves()

    def __len__(self):
        self.number_of_moves()

    def winner(self):
        if self.is_game_ended():
            return self.winner

    def who_plays(self):
        if self.turn == 1:
            return self.player1.getName()
        else:
            return self.player2.getName()
