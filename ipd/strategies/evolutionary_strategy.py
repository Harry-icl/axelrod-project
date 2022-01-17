from axelrod.action import Action
from axelrod.player import Player
from numpy.random import random

C, D = Action.C, Action.D


class EvolutionaryStrategy(Player):
    name = "Evo"
    classifier = {
        "memory_depth": 1,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, epsilon=0.05, lr=0.1):
        self.f = 1 - epsilon
        self.qR = 1 - epsilon
        self.qS = epsilon
        self.qT = 1 - epsilon
        self.qP = epsilon
        self.learning_rate = lr
        super().__init__()

    def strategy(self, opponent: Player) -> Action:
        if not self.history:
            self.last_prob = "f"
            if random() < self.f:
                return C
            else:
                return D
        if len(self.history) >= 2:
            if self.history[-2] == D and opponent.history[-1] == C:
                self.qR = (1 - self.learning_rate)*self.qR
                self.qT = (1 - self.learning_rate)*self.qT
            elif self.history[-2] == D and opponent.history[-1] == D:
                self.qR = 1 - (1 - self.learning_rate)*(1 - self.qR)
                self.qT = 1 - (1 - self.learning_rate)*(1 - self.qT)
            elif self.history[-2] == C and opponent.history[-1] == D:
                self.qS = (1 - self.learning_rate)*self.qS
                self.qP = (1 - self.learning_rate)*self.qS
            elif self.history[-2] == C and opponent.history[-1] == C:
                self.qS = 1 - (1 - self.learning_rate)*(1 - self.qS)
                self.qP = 1 - (1 - self.learning_rate)*(1 - self.qP)

        if self.history[-1] == C and opponent.history[-1] == C:
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
