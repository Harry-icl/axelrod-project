from axelrod.action import Action, actions_to_str
from axelrod.player import Player
from axelrod.strategy_transformers import (
    FinalTransformer,
    TrackHistoryTransformer,
)
from numpy.random import random

C, D = Action.C, Action.D


class MixedStrategy(Player):
    name = f"Mixed strategy"
    classifier = {
        "memory_depth": 1,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, f, p, q):
        self.f = f
        self.p = p
        self.q = q
        super().__init__()

    def strategy(self, opponent: Player) -> Action:
        if not self.history:
            if random() < self.f:
                return C
            else:
                return D
        elif opponent.history[-1] == C:
            if random() < self.p:
                return C
            else:
                return D
        elif opponent.history[-1] == D:
            if random() < self.q:
                return C
            else:
                return D


class MemoryOneStrategy(Player):
    name = "MOS"
    classifier = {
        "memory_depth": 1,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, f, qR, qS, qT, qP):
        self.f = f
        self.qR = qR
        self.qS = qS
        self.qT = qT
        self.qP = qP
        super().__init__()

    def strategy(self, opponent: Player) -> Action:
        if not self.history:
            if random() < self.f:
                return C
            else:
                return D
        elif self.history[-1] == C and opponent.history[-1] == C:
            if random() < self.qR:
                return C
            else:
                return D
        elif self.history[-1] == C and opponent.history[-1] == D:
            if random() < self.qS:
                return C
            else:
                return D
        elif self.history[-1] == D and opponent.history[-1] == C:
            if random() < self.qT:
                return C
            else:
                return D
        elif self.history[-1] == D and opponent.history[-1] == D:
            if random() < self.qP:
                return C
            else:
                return D
