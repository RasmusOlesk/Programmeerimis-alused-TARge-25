"""Zoo."""
from typing import List

from animal import Animal




class Zoo:
    """Zoo class."""

    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and max number of animals the zoo can have.
        There also should be an overview of all animals present in the zoo.

        :param name: zoo name
        :param max_number_of_animals: how many animals can be in the zoo
        """
        self.species = None
        self.max_number_of_animals = max_number_of_animals
        self.made = name
        self.zoo_animals: List[Animal] = []

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be added to the zoo.

        Animal can be added to the zoo if:
        1. Adding a new animal does not exceed zoo's max number of animals.
        2. Same Animal object is not present in the zoo.
        3. Animal with same name and specie is not yet present in the zoo.
        :param animal: animal who is checked
        :return: bool describing whether the animal can be added to the zoo or not
        """
        if self.zoo_is_full():
            return False
        if animal in self.zoo_animals:
            return False
        for other in self.zoo_animals:
            if animal.name == other.name and self.species == other.species:
                return False
        return True

    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal who is going to be added to the zoo
        Function does not return anything
        """
        if self.can_add_animal(animal):
            self.zoo_animals.append(animal)

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed from the zoo if animal is present in the zoo.

        :param animal: animal who is checked
        :return: bool describing whether animal can be removed from the zoo or not.
        """
        if animal in self.zoo_animals:
            return True
        return False

    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal who is going to be removed from the zoo.
        Function does not return anything
        """
        if self.can_remove_animal(animal):
            self.zoo_animals_remove(animal)

    def get_all_animals(self):
        """
        Return a list with all the animals in the zoo.

        :return: list of Animal objects
        """
        return self.zoo_animals[:]

    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        return sorted(self.zoo_animals, key=lambda a: a.age)

    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted (by name) alphabetically.

        :return: list of Animal objects sorted by name alphabetically
        """
        return sorted(self.zoo_animals, key=lambda a: a.name)

    def zoo_is_full(self):
        """Return true if zoo_animals list contains max_number_of_animals count of animals."""
        return len(self.zoo_animals)  >= self.max_number_of_animals

    def zoo_animals_remove(self, animal):
        pass
