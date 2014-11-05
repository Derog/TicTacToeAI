__author__ = 'derog'


class DumbBrain():
    def __init__(self):
        self.board_values = [[0 for j in range(3)] for i in range(3)]

    def __call__(self, *args, **kwargs):
        self.board_values = args[0]
        for j in range(3):
            for i in range(3):
                if self.board_values[i][j] == 0:
                    return (i, j)

        return (None, None)

        # TODO <Add more elements of this class>