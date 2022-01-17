from trading_game.tg import TradingTournament
import axelrod as axl
import matplotlib.pyplot as plt
from trading_game.tg.strategies.basic_strategies import AlwaysAA, AlwaysAB, AlwaysN, TitForTat


players = [AlwaysAA(), AlwaysN(), AlwaysAB(), TitForTat()]
tournament = TradingTournament(players, seed=1)
results = tournament.play()
print(results.ranked_names)
plot = axl.Plot(results)
plot.boxplot()
plt.show()
