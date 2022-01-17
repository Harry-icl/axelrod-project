from axelrod.action import Action
from axelrod.player import Player
from axelrod.strategy_transformers import (
    FinalTransformer,
    TrackHistoryTransformer,
)

C, D = Action.C, Action.D


class NTitsForTat(Player):
    def __init__(self, n):
        self.name = f"{n} Tits For Tat"
        self.n = n
        self.classifier = {
            "memory_depth": n,  # Four-Vector = (1.,0.,1.,0.)
            "stochastic": False,
            "long_run_time": False,
            "inspects_source": False,
            "manipulates_source": False,
            "manipulates_state": False,
        }
        super().__init__()

    def strategy(self, opponent: Player) -> Action:
        return D if D in opponent.history[- self.n:] else C
