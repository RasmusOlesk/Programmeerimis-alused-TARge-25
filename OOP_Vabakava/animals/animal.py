from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstraktne baas-klass kõigile loomadele.

    Demonstreeritavad OOP oskused:
    - Abstraktsioon: klass on abstraktne ja seda ei saa otse luua.
    - Pärilus: teised loomaklassid (Lion, Elephant, Monkey) pärivad sellest.
    - Kapseldus: terviseväärtus (_health) on kaitstud ja sellele pääseb ligi ainult getter/setteriga.

    Atribuudid:
        name (str): looma nimi.
        age (int): looma vanus.
        _health (int): looma tervis, väärtus 0–100.
    """

    def __init__(self, name, age):
        """
        Initsialiseerib looma põhiandmed.

        Args:
            name (str): looma nimi.
            age (int): looma vanus.

        Määrab tervise vaikimisi väärtuseks 100.
        """
        self.name = name
        self.age = age
        self._health = 100

    @abstractmethod
    def make_sound(self):
        """
        Abstraktne meetod, mis tagab polümorfismi.
        Iga loomaklass peab selle üle kirjutama ja tagastama looma hääle.

        Returns:
            str: looma hääl.
        """
        pass

    def get_health(self):
        """
        Tagastab looma terviseväärtuse.

        Returns:
            int: tervis vahemikus 0–100.
        """
        return self._health

    def set_health(self, value):
        """
        Määrab looma terviseväärtuse, kui see jääb lubatud vahemikku.

        Args:
            value (int): uus terviseväärtus (0–100).

        Kui väärtus on vale, ei muudeta tervist ja väljastatakse hoiatus.
        """
        if 0 <= value <= 100:
            self._health = value
        else:
            print("Tervise väärtus peab olema 0–100.")
