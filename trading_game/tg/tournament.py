from enum import Enum
from typing import Union, Tuple, List
from axelrod import Game, Tournament, Player
from numpy.random import random


Score = Union[int, float]


class TradingAction(Enum):
    AA = 0 # Aggressive ask
    N = 1 # Neutral
    AB = 2 # Aggressive bid


class TradingGame(Game):
    def __init__(self, k: Score = 1.5, f: Score = 3) -> None:
        """
        Create a new trading game object.
        
        Parameters
        ----------
        k: int or float
            The kickback for being a market maker.
        f: int or float
            The fee for being a market taker.
        """
        self.k = k
        self.f = f

    def get_payoffs(self, player1, player2):
        random1 = random()
        random2 = random()
        if player1 == TradingAction.AA and player2 == TradingAction.AA:
            return ((random1 < 0.5)*(1 + self.k) + (random2 < 0.5)*self.k,
                    (random1 >= 0.5)*(1 + self.k) + (random2 >= 0.5)*self.k)
        
        elif player1 == TradingAction.AA and player2 == TradingAction.N:
            return ((random1 < 0.5)*(1 + self.k) + self.k,
                    (random1 >= 0.5)*(1 + self.k))
        
        elif player1 == TradingAction.AA and player2 == TradingAction.AB:
            return (1 + self.k + (random1 < 0.5)*self.k - (random1 >= 0.5)*self.f,
                    1 + self.k + (random1 >= 0.5)*self.k - (random1 < 0.5)*self.f)
        
        elif player1 == TradingAction.N and player2 == TradingAction.AA:
            return ((random1 < 0.5)*(1 + self.k),
                    (random1 >= 0.5)*(1 + self.k) + self.k)
        
        elif player1 == TradingAction.N and player2 == TradingAction.N:
            return ((random1 < 0.5)*(1 + self.k) + (random2 < 0.5)*(1 + self.k),
                    (random1 >= 0.5)*(1 + self.k) + (random2 >= 0.5)*(1 + self.k))
        
        elif player1 == TradingAction.N and player2 == TradingAction.AB:
            return ((random2 < 0.5)*(1 + self.k),
                    self.k + (random2 >= 0.5)*(1 + self.k))
        
        elif player1 == TradingAction.AB and player2 == TradingAction.AA:
            return (1 + self.k + (random1 < 0.5)*self.k - (random1 >= 0.5)*self.f,
                    1 + self.k + (random1 >= 0.5)*self.k - (random1 < 0.5)*self.f)

        elif player1 == TradingAction.AB and player2 == TradingAction.N:
            return (self.k + (random2 < 0.5)*(1 + self.k),
                    (random2 >= 0.5)*(1 + self.k))
        
        elif player1 == TradingAction.AB and player2 == TradingAction.AB:
            return ((random1 < 0.5)*self.k + (random2 < 0.5)*(1 + self.k),
                    (random1 >= 0.5)*self.k + (random2 >= 0.5)*(1 + self.k))

    def score(self, pair: Tuple[TradingAction, TradingAction]) -> Tuple[Score, Score]:
        """
        Returns the appropriate score for a decision pair.
        
        Parameters
        ----------
        pair: tuple(Action, Action)
            A pair of actions for two players, for example, (AB, AB).
            
        Returns
        -------
        tuple of int or float
            Scores for two players resulting from their actions.
        """
        return self.get_payoffs(*pair)


class TradingTournament(Tournament):
    def __init__(
        self,
        players: List[Player],
        name: str = "Trading Tournament",
        game: TradingGame = None,
        turns: int = None,
        prob_end: float = None,
        repetitions: int = 10,
        noise: float = 0,
        edges: List[Tuple] = None,
        match_attributes: dict = None,
        seed: int = None
    ) -> None:
        if game is None:
            game = TradingGame()
        super().__init__(players, name, game, turns, prob_end, repetitions, noise, edges, match_attributes, seed)
