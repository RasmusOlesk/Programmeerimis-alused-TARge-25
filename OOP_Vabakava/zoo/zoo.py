class Zoo:
    """
    Zoo klass haldab loomade kogumit ning pakub meetodeid loomade lisamiseks,
    eemaldamiseks ja kuvamiseks.

    Demonstreeritavad OOP oskused:
        - Objektide haldamine listis (kompositsioon)
        - Meetodid süsteemi juhtimiseks
        - Andmestruktuuride kasutamine (list)
    """

    def __init__(self):
        """
        Initsialiseerib uue loomaaia.

        Loob tühja listi 'animals', kuhu lisatakse kõik loomad,
        mis kasutaja programmi käigus sisestab.
        """
        self.animals = []

    def add_animal(self, animal):
        """
        Lisab looma loomaaeda.

        Args:
            animal (Animal): looma objekt (Lion, Elephant, Monkey jne).

        Funktsioon lisab looma 'animals' listi ja väljastab kinnituse.
        """
        print(f"Lisan looma: {animal.name}")
        self.animals.append(animal)

    def remove_animal(self, name):
        """
        Eemaldab loomaaia listist kõik loomad, kelle nimi vastab kasutaja sisestusele.

        Args:
            name (str): kustutatava looma nimi.

        NB! Kui mitu looma kannavad sama nime, eemaldatakse kõik sama nimega loomad.
        Täpsem kustutamine toimub main.py failis, kus kasutaja saab valida konkreetse looma.
        """
        self.animals = [a for a in self.animals if a.name != name]
        print(f"Loom '{name}' eemaldatud.")

    def show_all(self):
        """
        Kuvab kõik loomad loomaaia listist.

        Iga looma kohta näidatakse:
            - nimi
            - liik (klass)
            - vanus
            - tervis
            - looma hääl (polümorfism)

        Kui loomi pole, ei kuvata midagi.
        """
        print("\n--- Loomaaia ülevaade ---")
        for a in self.animals:
            print(
                f"{a.name} ({a.__class__.__name__}), "
                f"vanus {a.age}, tervis {a.get_health()}, "
                f"hääl: {a.make_sound()}"
            )
