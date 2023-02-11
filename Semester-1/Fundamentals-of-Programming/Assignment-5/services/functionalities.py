from src.domain.student import Student


class Service:

    def __init__(self):
        self._list_of_students = []

    @property
    def list_of_students(self):
        return self._list_of_students

    @list_of_students.setter
    def list_of_students(self, students_list):
        self._list_of_students = students_list

    @staticmethod
    def initialize_list_of_10_students():
        return [Student(1, "Alex Pop", 912), Student(2, "Oana Ionescu", 913), Student(3, "Diana Munteanu", 912),
                Student(4, "Marius Ioan", 917), Student(5, "Darius Popescu", 915), Student(6, "Maria Neag", 917),
                Student(7, "Alexandru Iliescu", 916), Student(8, "Andreea Stan", 914), Student(9, "Ioana Lungu", 913),
                Student(10, "Andrei Radu", 916)]

    def add_student_to_list_of_students(self, student):
        """
            This function adds a new student to the list of students, only if the id does not already appear in the
        list of students.
        :param student: the student that needs to be added in the list of students
        """
        if not isinstance(student, Student):
            raise TypeError("Invalid type for student !")
        else:
            id_of_student_to_add = student.student_id
            list_of_students = self._list_of_students
            for current_student in list_of_students:
                current_student_id = current_student.student_id
                if id_of_student_to_add == current_student_id:
                    raise ValueError("This student's student_id already exists ! You cannot add it again!")
            self._list_of_students.append(student)

    def filter_list_of_students_by_group(self, given_group):
        """
            This function filters the list of students, so that the students in the given group are deleted from the
        list. It returns the number of students that are deleted, 0 in case there is no student from the given group.
        :param given_group: the given group to filter the list of students by
        :return: the number of students that are deleted, 0 in case there is no student from the given group
        """
        if isinstance(given_group, int):
            if given_group <= 0:
                raise ValueError("Invalid input for group !")
            students_list = self._list_of_students
            index = 0
            group_exists_in_list = 0
            while index < len(students_list):
                current_student = students_list[index]
                current_student_group = current_student.group
                if current_student_group == given_group:
                    group_exists_in_list += 1
                    students_list.pop(index)
                else:
                    index += 1
            return group_exists_in_list
        else:
            raise TypeError("Invalid type for group !")
