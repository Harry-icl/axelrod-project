import axelrod as axl
from tg import TradingTournament
import matplotlib.pyplot as plt
from numpy.random import random
from tg.strategies import MemoryOneStrategy

for _ in range(3):
    zd_strat_f = (0.5, 0.5)
    zd_strat_pAA = [0.5, 0.5, 0.5, 7 / 16, 0.5, 5 / 16, 0.5, 0.5, 0.5]
    zd_strat_pAB = [1, 15 / 16, 13 / 16, 1, 1, 1, 3 / 16, 3 / 16, 1 / 8]

    random_strat_f = (0.5, 0.5)
    random_trios = [random(3) for _ in range(9)]
    random_trios_rescaled = [x / sum(x) for x in random_trios]
    random_strat_pAA = [x[0] for x in random_trios_rescaled]
    random_strat_pAB = [x[1] for x in random_trios_rescaled]
        
    players = ([MemoryOneStrategy(zd_strat_f, zd_strat_pAA, zd_strat_pAB)]
            + [MemoryOneStrategy(random_strat_f, random_strat_pAA, random_strat_pAB)])
    tournament = TradingTournament(players, seed=1)
    results = tournament.play()
    print(results.ranked_names)
    plot = axl.Plot(results)
    plot.boxplot()
    plt.tight_layout()
    plt.show()

plot.payoff()
plt.tight_layout()
plt.show()
