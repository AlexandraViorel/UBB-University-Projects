from src.services.functionalities import Service
from src.domain.student import Student
from src.services.tests import run_all_tests


class UI:

    def __init__(self, service):
        self._functionalities = service
        self._list_of_versions_of_list_of_students = []
        self._list_of_operations = []

    def add_student_to_list_of_students_ui(self):
        """
            This function adds a student to the list of students. If there already exists a student with the same id
        given as input, it displays a message and it does not add the student to the list.
        """
        student_id = input("Write the id of the student: ")
        name = input("Write the name of the student: ")
        group = input("Write the group of the student: ")

        try:
            student_id = int(student_id)
        except ValueError:
            print("Invalid type for student id !")
            return

        try:
            group = int(group)
            if int(group) <= 0:
                raise ValueError("Invalid value for group !")
        except ValueError:
            print("Invalid type for group !")
            return

        try:
            self._list_of_versions_of_list_of_students.append(self._functionalities.list_of_students[:])
            self._functionalities.add_student_to_list_of_students(Student(student_id, name, group))
            print("Student added successfully !")
            self._list_of_operations.append("add student")
        except ValueError as ve:
            print(str(ve))
            self._list_of_versions_of_list_of_students.pop()

    def display_entire_list_of_students(self):
        list_of_students = self._functionalities.list_of_students
        if len(list_of_students) == 0:
            print("There are no students in the list !")
        else:
            for student in list_of_students:
                print(student)

    def filter_list_of_students_by_group_ui(self):
        """
            This function filters the list of students by a given group. If there are no students from the given group
        it displays a message. Also if the entire list of students is deleted it displays a message.
        """
        given_group = input("Write the group you want to delete from the list: ")
        try:
            given_group = int(given_group)
        except ValueError:
            print("Invalid type for group !")
            return
        try:
            self._list_of_versions_of_list_of_students.append(self._functionalities.list_of_students[:])
            given_group_exists_in_list = self._functionalities.filter_list_of_students_by_group(given_group)
            if given_group_exists_in_list == 0:
                print("There are no students in the given group ! The list isn't filtered !")
                self._list_of_versions_of_list_of_students.pop()
            else:
                print("List filtered successfully !")
                if len(self._functionalities.list_of_students) == 0:
                    print("All students were from group " + str(given_group) + " so the entire list was deleted !")
                self._list_of_operations.append("filter")
        except ValueError as ve:
            print(str(ve))
            self._list_of_versions_of_list_of_students.pop()

    def undo_last_operation(self):
        """
            This function undoes the last operation executed that modified the list of students. If there are no
        operations to undo, it displays a message.
        """
        if len(self._list_of_versions_of_list_of_students) == 0:
            print("There are no operations to undo !")
        else:
            last_operation = self._list_of_operations[len(self._list_of_operations) - 1]
            print("The operation to undo is: " + last_operation)
            last_version_of_students_list = self._list_of_versions_of_list_of_students[len(self._list_of_versions_of_list_of_students) - 1]
            self._functionalities._list_of_students = last_version_of_students_list
            self._list_of_versions_of_list_of_students.pop()
            self._list_of_operations.pop()
            print("Operation undone successfully !")

    @staticmethod
    def print_menu():
        """
            This function prints the menu.
        """
        print("--- OPTIONS MENU --- ")
        print("1. Add student ")
        print("2. Display the list of students ")
        print("3. Filter the list of students ")
        print("4. Undo last operation ")
        print("5. Exit")

    def start(self):
        run_all_tests()
        self._functionalities._list_of_students = Service.initialize_list_of_10_students()
        while True:
            UI.print_menu()
            option = input("Your option is > ")

            if option == "1":
                self.add_student_to_list_of_students_ui()
            elif option == "2":
                self.display_entire_list_of_students()
            elif option == "3":
                self.filter_list_of_students_by_group_ui()
            elif option == "4":
                self.undo_last_operation()
            elif option == "5":
                return
            else:
                print("Invalid option ! Try again !")


service1 = Service()
ui = UI(service1)
ui.start()
