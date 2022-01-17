import axelrod as axl
import matplotlib.pyplot as plt
import numpy as np
from strategies.mixed_strategy import MemoryOneStrategy
from itertools import product

lim_probs = [0, 1]
probs = [0, 0.33, 0.66, 1]
param_names = ["f", "qR", "qS", "qT", "qP"]

prob_set = [probs]*5
players = [MemoryOneStrategy(f, qR, qS, qT, qP, name=(f, qR, qS, qT, qP)) for f, qR, qS, qT, qP in product(*prob_set)]
tournament = axl.Tournament(players, seed=1)
results = tournament.play()

for i in range(5):
    params = [eval(name)[i] for name in results.ranked_names]
    scores = sorted([np.nanmedian(norm_scores) for norm_scores in results.normalised_scores], reverse=True)
    plt.scatter(params, scores)
    plt.xlabel(param_names[i])
    plt.ylabel("Average score in tournament")
    plt.show()
