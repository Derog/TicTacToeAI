__author__ = 'derog'

import fileinput


class Board():
    def __init__(self):
        # 0 empty, 1 first player, -1 second player
        self._board_values = [[0 for j in range(3)] for i in range(3)]
        self._is_game_not_ended = True
        self._number_of_moves = 0
        self.winner = 0

    def value(self, xposition, yposition):
        return self._board_values[xposition][yposition]

    def values(self):
        return self._board_values

    def load(self, values):
        self._board_values = values[:]

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

        # First check if there are avaible slots to play in, since we have the number of moves this is easy
        if self.number_of_moves() == 9:
            self._is_game_not_ended = False

        # Now we will check if someone wins the game; we will search only for the player playing
        def win_check(position, value, vector=(0, 0)):
            # Check if the position is valid
            x = position[0]
            y = position[1]
            if x < 0 or y < 0 or x > 2 or y > 2:
                return 0
            else:
                if vector == (0, 0):
                    #First time execution
                    if self._board_values[x][y] == value:
                        max_value = 0
                        vector_list = [(1, 0), (0, 1), (1, 1), (1, -1)]
                        for element in vector_list:
                            #Reevaluates with all the displacements
                            temp = 0
                            temp = win_check((x + element[0], y + element[1]), value, element)
                            temp += win_check((x - element[0], y - element[1]), value, (-element[0], -element[1]))
                            if temp > max_value:
                                max_value = temp
                        return 1 + max_value
                    else:
                        raise ValueError("Function should be used if the first position/value is wrong")
                else:
                    #Recursive values
                    if self._board_values[x][y] == value:
                        return 1 + win_check((x + vector[0], y + vector[1]), value, vector)
                    else:
                        return 0

        if win_check((xposition, yposition), value) > 2:
            self._is_game_not_ended = False
            self.winner = value


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
        return self._numeer_of_moves

    def who_wins(self):
        return self.winner


class Player():
    def __init__(self, name="", brain=None, human=False):
        self.name = name
        self._is_human = human
        self.comp_time = []
        if name == "" and brain != None:
            self.name = str(brain)
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

    def get_average_time(self):
        return sum(self.comp_time) / len(self.comp_time)

    def move(self, board, lastmove, player):
        import time

        start = time.clock()
        if self.is_human():
            move = []
            move[0] = fileinput.input()
            move[1] = fileinput.input()
            self.comp_time.append((time.clock() - start))
            return move
        else:
            if self.has_brain():
                play = self.brain(board, lastmove, player)
                self.comp_time.append((time.clock() - start))
                return play
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
        self._winner = 0
        self.lastmove = (None, None)

    def move(self):
        if self.turn == 1:
            self.lastmove = self.player1.move(self.board.getBoardValues(), self.lastmove, self.turn)
        else:
            self.lastmove = self.player2.move(self.board.getBoardValues(), self.lastmove, self.turn)

        self.board.move(self.lastmove[0], self.lastmove[1], self.turn)
        self.turn *= -1

        if not self.board.is_game_notended():
            self._winner = self.board.who_wins()


    def __bool__(self):
        return self.is_game_notended()

    def __str__(self):
        text = 'Player1[X] is ' + self.player1.getName() + '\n'
        text += 'Player2[O] is ' + self.player2.getName() + '\n'
        text += str(self.board)
        return text

    def __iter__(self):
        self.move()

    def is_game_notended(self):
        return self.board.is_game_notended()

    def number_of_moves(self):
        return self.board.number_of_moves()

    def __len__(self):
        self.number_of_moves()

    def winner(self):
        if self.is_game_notended():
            return "No one won yet"
        else:
            if self._winner == 1:
                return self.player1.getName()
            elif self._winner == 0:
                return "Draw"
            else:
                return self.player2.getName()

    def who_plays(self):
        if self.turn == 1:
            return self.player1.getName()
        else:
            return self.player2.getName()

            #TODO <Short the wasted time>