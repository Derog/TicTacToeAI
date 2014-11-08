__author__ = 'derog'

import TicTacToeGame


class DumbBrain():
    def __init__(self):
        self.board_values = [[0 for j in range(3)] for i in range(3)]

    def __str__(self):
        return 'DumbBrain'

    def __call__(self, *args, **kwargs):
        self.board_values = args[0]
        for j in range(3):
            for i in range(3):
                if self.board_values[i][j] == 0:
                    return (i, j)

        return (None, None)


class RandomBrain():
    def __init__(self):
        self.board_values = [[0 for j in range(3)] for i in range(3)]

    def __str__(self):
        return 'RandomBrain'

    def __call__(self, *args, **kwargs):
        self.board_values = args[0]
        # First make a list with all the empty slots
        empty_slots = []
        for j in range(3):
            for i in range(3):
                if self.board_values[i][j] == 0:
                    empty_slots.append((i, j))
        import random

        return random.choice(empty_slots)
        return (None, None)


class FirstTree():
    def __init__(self):
        self.board_values = TicTacToeGame.Board()

    def __str__(self):
        return 'FirstTree'

    def __call__(self, *args, **kwargs):
        self.board_values.load(args[0])
        player = args[2]
        # First make a list with all the empty slots
        empty_slots = []
        for j in range(3):
            for i in range(3):
                if self.board_values.value(i, j) == 0:
                    empty_slots.append((i, j))

        from copy import deepcopy
        # For all this plays search for one of them that wins
        for play in empty_slots:
            test_board = deepcopy(self.board_values)
            test_board.move(play[0], play[1], player)
            if test_board.who_wins() == player:
                return play

        import random

        return random.choice(empty_slots)
        return (None, None)


class FisrtTreeDouble():
    def __init__(self):
        self.board_values = TicTacToeGame.Board()

    def __str__(self):
        return 'FisrtTreeDouble'

    def __call__(self, *args, **kwargs):
        self.board_values.load(args[0])
        player = args[2]
        # First make a list with all the empty slots
        empty_slots = []
        for j in range(3):
            for i in range(3):
                if self.board_values.value(i, j) == 0:
                    empty_slots.append((i, j))

        from copy import deepcopy
        # For all this plays search for one of them that wins
        for play in empty_slots:
            test_board = deepcopy(self.board_values)
            test_board.move(play[0], play[1], player)
            if test_board.who_wins() == player:
                return play

        #For all this plays search for one of them that looses, and try to avoid it
        for play in empty_slots:
            test_board = deepcopy(self.board_values)
            test_board.move(play[0], play[1], player * (-1))
            if test_board.who_wins() == player * (-1):
                return play

        import random

        return random.choice(empty_slots)
        return (None, None)

        #TODO <2r Tree equivalent to the up version to be honest>