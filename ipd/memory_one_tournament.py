import axelrod as axl
import matplotlib.pyplot as plt
from strategies.mixed_strategy import MemoryOneStrategy
from itertools import product

lim_probs = [0, 1]
probs = [0, 0.4, 0.6, 1]

for i in range(5):
    prob_set = [lim_probs]*5
    prob_set[i] = probs
    players = [MemoryOneStrategy(f, qR, qS, qT, qP) for f, qR, qS, qT, qP in product(*prob_set)]
    tournament = axl.Tournament(players, seed=1)
    results = tournament.play()
    print(results.ranked_names)
    plot = axl.Plot(results)
    plot.boxplot()
    plt.show()
