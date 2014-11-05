__author__ = 'derog'

import TicTacToeGame
import TicTacToeBrain

Bot1 = TicTacToeGame.Player('DumbBot1', TicTacToeBrain.DumbBrain())
Bot2 = TicTacToeGame.Player('DumbBot2', TicTacToeBrain.DumbBrain())

SimpleGame = TicTacToeGame.Game(Bot1, Bot2)

while SimpleGame:
    SimpleGame.move()
    print(SimpleGame)

print('Game Ended With Winner: ' + SimpleGame.winner())

# TODO <Add an statistical game mode in order to check different results>
#TODO <Add a time methos in order to evaluate processing times>