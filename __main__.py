from random_agent import RandomAgent
from game import Game
from agent import Agent
from ModelBasedAgent import MAgent

loop = 10
for i in range(10):
        count = 0
        agents = [
        RandomAgent(name='r1'),  
        RandomAgent(name='r2'),
        RandomAgent(name='r3'),   
        MAgent(name='Elon1'),   
        MAgent(name='Elon2'),
        MAgent(name='Elon3'),
        MAgent(name='Elon4')]
        game = Game(agents)
        game.play()
        



