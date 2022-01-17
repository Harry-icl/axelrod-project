from axelrod import Player
from tg.tournament import TradingAction


AA, N, AB = TradingAction.AA, TradingAction.N, TradingAction.AB


class AlwaysAA(Player):
    name = "Always Aggressive Ask"
    classifier = {
        "memory_depth": 0,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self):
        super().__init__()

    @staticmethod
    def strategy(opponent: Player) -> TradingAction:
        return AA


class AlwaysN(Player):
    name = "Always Neutral Pricing"
    classifier = {
        "memory_depth": 0,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self):
        super().__init__()

    @staticmethod
    def strategy(opponent: Player) -> TradingAction:
        return N


class AlwaysAB(Player):
    name = "Always Aggressive Bid"
    classifier = {
        "memory_depth": 0,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self):
        super().__init__()

    @staticmethod
    def strategy(opponent: Player) -> TradingAction:
        return AB


class TitForTat(Player):
    name = "Tit For Tat"
    classifier = {
        "memory_depth": 1,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self):
        super().__init__()

    def strategy(self, opponent: Player) -> TradingAction:
        """This is the actual strategy"""
        # First move
        if not self.history:
            return N
        # React to the opponent's last move
        if opponent.history[-1] == AA:
            return AA
        elif opponent.history[-1] == AB:
            return AB
        else:
            return N
