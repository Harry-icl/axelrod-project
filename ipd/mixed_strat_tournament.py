import axelrod as axl
import matplotlib.pyplot as plt
from strategies.mixed_strategy import MixedStrategy
from itertools import product

probs = [0, 0.4, 0.6, 1]
print(len([x for x in product(probs, probs, probs)]))

players = [MixedStrategy(f, p, q) for f, p, q in product(probs, probs, probs)]
tournament = axl.Tournament(players, seed=1)
results = tournament.play()
print(results.ranked_names)
plot = axl.Plot(results)
plot.boxplot()
plt.show()
