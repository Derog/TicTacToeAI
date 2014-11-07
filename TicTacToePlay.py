__author__ = 'derog'

import TicTacToeGame
import TicTacToeBrain


def SingleBotGame(brain1, brain2):
    Bot1 = TicTacToeGame.Player(brain=brain1)
    Bot2 = TicTacToeGame.Player(brain=brain2)

    SimpleGame = TicTacToeGame.Game(Bot1, Bot2)

    while SimpleGame:
        SimpleGame.move()
        print(SimpleGame)

    print('Game Ended With Winner: ' + SimpleGame.winner())


def BotStats(brain1, brain2):
    Bot1 = TicTacToeGame.Player(brain=brain1)
    Bot2 = TicTacToeGame.Player(brain=brain2)
    import time

    start = time.clock()

    results = []
    ngames = 10000
    for i in range(ngames):
        SimpleGameStat = TicTacToeGame.Game(Bot1, Bot2)
        while SimpleGameStat:
            SimpleGameStat.move()
        results.append(SimpleGameStat.winner())

    stats = {}
    stats[Bot1.getName()] = 0
    stats[Bot2.getName()] = 0
    stats["Draw"] = 0
    for element in results:
        stats[element] += 1

    print(Bot1.getName() + ' winrate is: ' + str(stats[Bot1.getName()] * 100 / ngames))
    print(Bot1.getName() + ' avg comp time is: ' + str(Bot1.get_average_time()))
    print(Bot2.getName() + ' winrate is: ' + str(stats[Bot2.getName()] * 100 / ngames))
    print(Bot2.getName() + ' avg comp time is: ' + str(Bot2.get_average_time()))
    print('Draw winrate is: ' + str(stats["Draw"] * 100 / ngames))
    print('Processing average time is: ' + str((time.clock() - start) / ngames))


SingleBotGame(TicTacToeBrain.FirstTree(), TicTacToeBrain.RandomBrain())
BotStats(TicTacToeBrain.FirstTree(), TicTacToeBrain.RandomBrain())

# TODO <Build an stat table>