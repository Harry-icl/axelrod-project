import axelrod as axl
import matplotlib.pyplot as plt
from strategies.ntitsfortat import NTitsForTat


for setup in [(1, 1), (1, 10), (10, 1), (10, 10)]:
    players = [axl.Cooperator()]*setup[0] + [axl.Defector()]*setup[1] + [NTitsForTat(n) for n in range(1, 11)]
    tournament = axl.Tournament(players, seed=1)
    results = tournament.play()
    print(results.ranked_names)
    plot = axl.Plot(results)
    plot.boxplot()
    plt.show()
