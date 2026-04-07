"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    __STATUS_ACTIVE = "Active"
    __STATUS_EXPELLED = "Expelled"
    __STATUS_FINISHED = "Finished"
    __STATUS_INACTIVE = "Inactive"

    def __init__(self, name: str, id: int):
        """Initialize student object."""
        self.__id = id
        self.__name = name
        self.__status = Student.__STATUS_ACTIVE

    def get_id(self) -> int:
        """Return student id."""
        return self.__id

    def set_name(self, name: str) -> None:
        """Set the name of the student."""
        self.__name = name

    def get_name(self) -> str:
        """Return student name."""
        return self.__name

    def get_status(self) -> str:
        """Return student status."""
        return self.__status

    def set_status(self, status: str) -> None:
        """Set the status of the student only if given status is correct."""
        allowed_statuses = [Student.__STATUS_ACTIVE, Student.__STATUS_EXPELLED, Student.__STATUS_FINISHED, Student.__STATUS_INACTIVE]
        if status in allowed_statuses:
            self.__status = status


if __name__ == '__main__':
    student1 = Student("Tiit", 1)
    print(student1.get_status())
    student1.set_status("lahkunud")
    print(student1.get_status())
    student1.set_status(Student.__STATUS_FINISHED)
    print(student1.get_status())