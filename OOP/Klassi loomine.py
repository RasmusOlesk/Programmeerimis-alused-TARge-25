"""Klassi ja Objekti harjutus."""


class Teacher:

    def __init__(self):
        super().__init__()
        self.school = []
        self.groups = []
        self.subjects = []


class Student:
    """Student class."""

    def __init__(self, name, finished=False):
        """Constructor for Student instance."""
        self.name = name
        self.finished = finished


if __name__ == '__main__':
    student_1 = Student()
    student = Student("John")
    print(student.name)  # John
    print(student.finished)  # False