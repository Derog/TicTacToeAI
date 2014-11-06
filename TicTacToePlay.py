__author__ = 'derog'

import TicTacToeGame
import TicTacToeBrain

Bot1 = TicTacToeGame.Player('DumbBot1', TicTacToeBrain.RandomBrain())
Bot2 = TicTacToeGame.Player('DumbBot2', TicTacToeBrain.RandomBrain())

SimpleGame = TicTacToeGame.Game(Bot1, Bot2)

while SimpleGame:
    SimpleGame.move()
    print(SimpleGame)

print('Game Ended With Winner: ' + SimpleGame.winner())

import time

start = time.clock()


results=[]
ngames=10000
for i in range(ngames):
    SimpleGameStat = TicTacToeGame.Game(Bot1, Bot2)
    while SimpleGameStat:
        SimpleGameStat.move()
    results.append(SimpleGameStat.winner())

stats={}
stats[Bot1.getName()]=0
stats[Bot2.getName()]=0
stats["Draw"]=0
for element in results:
    stats[element]+=1

print(Bot1.getName() +' winrate is: '+str(stats[Bot1.getName()]*100/ngames))
print(Bot2.getName() +' winrate is: '+str(stats[Bot2.getName()]*100/ngames))
print('Draw winrate is: '+str(stats["Draw"]*100/ngames))
print('Processing average time is: '+ str((time.clock() - start)/ngames))

#TODO <Establish some functions to clarify the code>+
#TODO <Time Methods for Each AI>
#TODO <Automatic Names for AI>