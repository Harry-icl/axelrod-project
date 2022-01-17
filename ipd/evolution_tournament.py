import axelrod as axl
import matplotlib.pyplot as plt
from numpy.random import random
from strategies.mixed_strategy import MemoryOneStrategy
from strategies.evolutionary_strategy import EvolutionaryStrategy

zd_strat = [round(x, 3) for x in [random(), 11 / 13, 1 / 2, 7 / 26, 0]]
    
players = ([MemoryOneStrategy(*zd_strat)]
           + [MemoryOneStrategy(1, 1, 0, 1, 0)]
           + [EvolutionaryStrategy()])
tournament = axl.Tournament(players, seed=1)
results = tournament.play()
print(results.ranked_names)
plot = axl.Plot(results)
plot.boxplot()
plt.tight_layout()
plt.show()

plot.payoff()
plt.tight_layout()
plt.show()
