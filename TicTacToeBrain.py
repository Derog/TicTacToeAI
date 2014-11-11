__author__ = 'derog'

import TicTacToeGame
import random


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

        # For all this plays search for one of them that looses, and try to avoid it
        for play in empty_slots:
            test_board = deepcopy(self.board_values)
            test_board.move(play[0], play[1], player * (-1))
            if test_board.who_wins() == player * (-1):
                return play

        import random

        return random.choice(empty_slots)
        return (None, None)


class DerogBrain():
    def __init__(self):
        self.board_values = TicTacToeGame.Board()

    def __str__(self):
        return 'DerogBrain'

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

        # For all this plays search for one of them that looses, and try to avoid it
        for play in empty_slots:
            test_board = deepcopy(self.board_values)
            test_board.move(play[0], play[1], player * (-1))
            if test_board.who_wins() == player * (-1):
                return play

        if (1, 1) in empty_slots:
            return (1, 1)

        corner = [(0, 0), (2, 0), (0, 2), (2, 2)]
        if corner in empty_slots:
            return random.choice(corner)

        return random.choice(empty_slots)


# Node class to simplify the notation that we will use, since Python calls code in realtime we cant call a class from itself
#There fore we must call two independent classes from where we can do so explicetly
class BoardNode():
    def __init__(self, board, turn):
        self.parent = None
        self.value = None
        self.play = (None, None)
        self.board = board
        self.turn = turn
        self.childs = []

    def __str__(self):
        return str(self.board)

    def getValue(self):
        pass


class TreeBoardNode():
    def __init__(self, board, turn, maxdeep=2):
        self.player = turn
        temp = TicTacToeGame.Board()
        temp.load(board)
        self.maxdeep = maxdeep
        self.root = BoardNode(temp, turn)
        self.create_subtree(self.root)


    def create_subtree(self, node, deep=0):
        if deep < self.maxdeep:
            empty_slots = []
            for j in range(3):
                for i in range(3):
                    if node.board.value(i, j) == 0:
                        empty_slots.append((i, j))

            from copy import deepcopy
            # For all this plays search for one of them that wins
            for play in empty_slots:
                test_board = deepcopy(node.board)
                test_board.move(play[0], play[1], node.turn)
                test_child = BoardNode(test_board, node.turn * (-1))
                test_child.play = play
                test_child.parent = node
                node.childs.append(test_child)
                if test_board.is_game_notended():
                    self.create_subtree(test_child, deep + 1)

    def load_values(self, node):
        #Build a value list for the elements
        #If it has childs, fills the childs values and apply min/max
        if len(node.childs) > 0:
            #Value List
            vlist = []
            for child in node.childs:
                if child.value == None:
                    self.load_values(child)
                #Since concept of max min depend of our number
                vlist.append(child.value)
            vlist.sort()
            if node.turn == 1:
                #We take the min
                node.value = vlist[-1]
            else:
                #We take the max
                node.value = vlist[0]

        else:
            node.value = node.board.winner

    def chooseplay(self):
        self.load_values(self.root)
        possible_moves = []
        for child in self.root.childs:
            if child.value == self.root.value:
                possible_moves.append(child.play)

        return random.choice(possible_moves)


    def emptyvalues(self, node):
        node.value = None
        for child in node.childs:
            self.emptyvalues(child)

    def Update(self, play):
        pass


class BreathTree():
    def __init__(self, deep=2):
        self.tree_board = None
        self.maxdeep = deep

    def __str__(self):
        return 'BreathTree'


    def __call__(self, *args, **kwargs):
        self.tree_board = TreeBoardNode(args[0], args[2], self.maxdeep)
        play = self.tree_board.chooseplay()
        return play

        #TODO <Improve ram consumption and processing time, ram is clearly wasted>