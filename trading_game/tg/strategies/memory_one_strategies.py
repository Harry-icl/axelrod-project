from typing import Tuple
from tg.tournament import TradingAction
from axelrod.player import Player
from numpy.random import random


AA, AB, N = TradingAction.AA, TradingAction.AB, TradingAction.N


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

    def __init__(self, f: Tuple[int, int], pAA, pAB):
        self.f = f
        self.pAA = pAA
        self.pAB = pAB
        super().__init__()

    def strategy(self, opponent: Player) -> TradingAction:
        random1 = random()
        if not self.history:
            if random1 < self.f[0]:
                return AA
            elif random1 < self.f[0] + self.f[1]:
                return AB
            else:
                return N
        elif self.history[-1] == AA and opponent.history[-1] == AA:
            if random1 < self.pAA[0]:
                return AA
            elif random1 < self.pAA[0] + self.pAB[0]:
                return AB
            else:
                return N
        elif self.history[-1] == AA and opponent.history[-1] == AB:
            if random1 < self.pAA[1]:
                return AA
            elif random1 < self.pAA[1] + self.pAB[1]:
                return AB
            else:
                return N
        elif self.history[-1] == AA and opponent.history[-1] == N:
            if random1 < self.pAA[2]:
                return AA
            elif random1 < self.pAA[2] + self.pAB[2]:
                return AB
            else:
                return N
        elif self.history[-1] == AB and opponent.history[-1] == AA:
            if random1 < self.pAA[3]:
                return AA
            elif random1 < self.pAA[3] + self.pAB[3]:
                return AB
            else:
                return N
        elif self.history[-1] == AB and opponent.history[-1] == AB:
            if random1 < self.pAA[4]:
                return AA
            elif random1 < self.pAA[4] + self.pAB[4]:
                return AB
            else:
                return N
        elif self.history[-1] == AB and opponent.history[-1] == N:
            if random1 < self.pAA[5]:
                return AA
            elif random1 < self.pAA[5] + self.pAB[5]:
                return AB
            else:
                return N
        elif self.history[-1] == N and opponent.history[-1] == AA:
            if random1 < self.pAA[6]:
                return AA
            elif random1 < self.pAA[6] + self.pAB[6]:
                return AB
            else:
                return N
        elif self.history[-1] == N and opponent.history[-1] == AB:
            if random1 < self.pAA[7]:
                return AA
            elif random1 < self.pAA[7] + self.pAB[7]:
                return AB
            else:
                return N
        elif self.history[-1] == N and opponent.history[-1] == N:
            if random1 < self.pAA[8]:
                return AA
            elif random1 < self.pAB[8]:
                return AB
            else:
                return N
