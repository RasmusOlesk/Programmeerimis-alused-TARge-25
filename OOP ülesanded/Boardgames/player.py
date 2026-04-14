"""Player class"""

class player:
    """Player class."""

    def __init__(self, name: str):
        self.__name = name
        self.__games = []


    def get_played_game_count(self) -> int:
        """Return the amount of games played.

        "/player/{name}/amount" - tagastab int-i, mis kirjeldab, mitu mängu on mängija nimega player_
        """

        return len(self.__games)

    def get_favorite_game_name(self) -> str:
        """
        Return the name of the game most played.

        "/player/{name}/favotite" - tagastab mängu (str, kus on mängu nimi), mida mängija nimega player_n
        """

        pass

    def get_won_game_count(self) -> int:
        """
        Return the amount of games played
        """

    def get_won_game_count(self) -> int:



    def get_name(self):

        return