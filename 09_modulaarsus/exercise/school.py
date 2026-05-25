class School:

    def __init__(self, name: str):
        self.__name = name

    def add_student(self, student: Student):
        pass

    def get_students(self) -> list[Student]:
        pass

    def add_course(self, course: Course):
        pass

    def get_courses(self) -> list[Course]:
        pass

    def add_student_grade(self, student: Student, course: Course, grade: int):
        pass

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        pass

   