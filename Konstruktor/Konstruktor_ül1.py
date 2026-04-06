"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Represent person with firstname, lastname and age."""
        super().__init__()
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Represent student with firstname, lastname and age."""
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    empty_object = Empty()
    p1 = Person()
    p1.firstname = "Tiit"
    p1.lastname = "Sukk"
    p1.age = 5
    p2 = Person()
    p2.firstname = "Teet"
    p2.lastname = "tukk"
    p2.age = 15
    p3 = Person()
    p3.firstname = "Peep"
    p3.lastname = "Lukk"
    p3.age = 25
    s1 = Student("Mari", "Maasikas", 13)
    s2 = Student("Kati", "Kaalikas", 12)
    s3 = Student("Tõnu", "Tõru", 11)
