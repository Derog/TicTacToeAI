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


from math import log10, floor


def round_sig(x, sig=1):
    return round(x, sig - int(floor(log10(x))) - 1)


def BotStats(brain1, brain2):
    Bot1 = TicTacToeGame.Player(brain=brain1)
    Bot2 = TicTacToeGame.Player(brain=brain2)
    import time

    ngames = 500
    start = time.clock()

    results_first = []

    for i in range(ngames):
        SimpleGameStat = TicTacToeGame.Game(Bot1, Bot2)
        while SimpleGameStat:
            SimpleGameStat.move()
        results_first.append(SimpleGameStat.winner())

    stats_first = {}
    stats_first[Bot1.getName()] = 0
    stats_first[Bot2.getName()] = 0
    stats_first["Draw"] = 0
    for element in results_first:
        stats_first[element] += 1

    wr_11 = str(stats_first[Bot1.getName()] * 100 / ngames)
    tr_11 = Bot1.get_average_time()
    wr_12 = str(stats_first[Bot2.getName()] * 100 / ngames)
    tr_12 = Bot2.get_average_time()
    wr_13 = str(stats_first["Draw"] * 100 / ngames)

    Bot1 = TicTacToeGame.Player(brain=brain2)
    Bot2 = TicTacToeGame.Player(brain=brain1)

    results_second = []
    for i in range(ngames):
        SimpleGameStat = TicTacToeGame.Game(Bot1, Bot2)
        while SimpleGameStat:
            SimpleGameStat.move()
        results_second.append(SimpleGameStat.winner())

    stats_second = {}
    stats_second[Bot1.getName()] = 0
    stats_second[Bot2.getName()] = 0
    stats_second["Draw"] = 0
    for element in results_second:
        stats_second[element] += 1

    wr_21 = str(stats_second[Bot1.getName()] * 100 / ngames)
    tr_21 = Bot1.get_average_time()
    wr_22 = str(stats_second[Bot2.getName()] * 100 / ngames)
    tr_22 = Bot2.get_average_time()
    wr_23 = str(stats_second["Draw"] * 100 / ngames)

    tr1 = (tr_11 + tr_22) / 2
    tr2 = (tr_12 + tr_21) / 2

    tr1 = round_sig(tr1 * ngames * 2)
    tr2 = round_sig(tr2 * ngames * 2)

    print('       ' + Bot2.getName() + '[' + str(tr1) + 's]' + '  ' + Bot1.getName() + '[' + str(
        tr2) + 's]' + '  ' + 'Draw')
    print('First: ' + wr_11 + ' ' * (len(Bot2.getName()) - len(wr_11) + len(str(tr1)) + 5) + wr_12 + ' ' * (
    len(Bot1.getName()) - len(wr_12) + len(str(tr2)) + 5) + wr_13)
    print('Secon: ' + wr_22 + ' ' * (len(Bot2.getName()) - len(wr_22) + len(str(tr1)) + 5) + wr_21 + ' ' * (
    len(Bot1.getName()) - len(wr_21) + len(str(tr2)) + 5) + wr_23)
    print('TTime: ' + str(round_sig(time.clock() - start, 2)) + 's')
    print('WTime: ' + str(round_sig(time.clock() - start - tr1 - tr2, 2)) + 's')


SingleBotGame(TicTacToeBrain.FisrtTreeDouble(), TicTacToeBrain.FirstTree())
BotStats(TicTacToeBrain.FisrtTreeDouble(), TicTacToeBrain.FirstTree())

# TODO <Short the code, and clean up the single game version>