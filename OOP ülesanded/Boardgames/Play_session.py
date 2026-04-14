from player import Player
from game import Game


class PlaySession:
    def __init__(self, filename: str):
        self.__players : dict[Player, GameResult] = {}
        self.__game : Game = game