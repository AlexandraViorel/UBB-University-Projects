from src.domain.student import Student
from src.services.functionalities import Service


def addStudentToListOfStudents_CorrectInputForAllVariables_ListWithStudentAdded():
    service = Service()
    service.list_of_students = []
    service.add_student_to_list_of_students(Student(1, "Andrei", 917))
    assert len(service.list_of_students) == 1


def addStudentToListOfStudents_StudentWithIdAlreadyInList_ValueError():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    try:
        service.add_student_to_list_of_students(Student(1, "Andrei", 917))
        assert False
    except ValueError:
        assert True


def addStudentToListOfStudents_AStringInput_TypeError():
    service = Service()
    service.list_of_students = []
    try:
        service.add_student_to_list_of_students("Andrei")
        assert False
    except TypeError:
        assert True


def addStudentToListOfStudents_AIntegerInput_TypeError():
    service = Service()
    service.list_of_students = []
    try:
        service.add_student_to_list_of_students(12)
        assert False
    except TypeError:
        assert True


def addStudentToListOfStudents_AFloatInput_TypeError():
    service = Service()
    service.list_of_students = []
    try:
        service.add_student_to_list_of_students(12.5)
        assert False
    except TypeError:
        assert True


def addStudentToListOfStudents_AListInput_TypeError():
    service = Service()
    service.list_of_students = []
    try:
        service.add_student_to_list_of_students([1, 2, 3])
        assert False
    except TypeError:
        assert True


def addStudentToListOfStudents_ADictionaryInput_TypeError():
    service = Service()
    service.list_of_students = []
    try:
        service.add_student_to_list_of_students({"id": 1, "name": "Andrei", "group": 917})
        assert False
    except TypeError:
        assert True


def addStudentToListOfStudents_StudentWithNameAlreadyInList_ListWithStudentAdded():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    service.add_student_to_list_of_students(Student(2, "Andrei", 912))
    assert len(service.list_of_students) == 2


def addStudentToListOfStudents_StudentWithGroupAlreadyInList_ListWithStudentAdded():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    service.add_student_to_list_of_students(Student(2, "Andreea", 917))
    assert len(service.list_of_students) == 2


def test_add_student_to_list_of_students():
    addStudentToListOfStudents_CorrectInputForAllVariables_ListWithStudentAdded()
    addStudentToListOfStudents_StudentWithIdAlreadyInList_ValueError()
    addStudentToListOfStudents_AStringInput_TypeError()
    addStudentToListOfStudents_AIntegerInput_TypeError()
    addStudentToListOfStudents_AFloatInput_TypeError()
    addStudentToListOfStudents_AListInput_TypeError()
    addStudentToListOfStudents_ADictionaryInput_TypeError()
    addStudentToListOfStudents_StudentWithNameAlreadyInList_ListWithStudentAdded()
    addStudentToListOfStudents_StudentWithGroupAlreadyInList_ListWithStudentAdded()


def filterListOfStudentsByGroup_AGroupThatExistsInTheList_HowManyStudentsAreInThatGroupAndTheListWillModify():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    assert service.filter_list_of_students_by_group(917) == 1
    assert len(service.list_of_students) == 0


def filterListOfStudentsByGroup_AGroupThatDoesNotExistInTheList_0AndTheListUnmodified():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    assert service.filter_list_of_students_by_group(916) == 0
    assert len(service.list_of_students) == 1


def filterListOfStudentsByGroup_AGroupThatExistsInTheList_HowManyStudentsAreInThatGroupAndTheListWithTheRemainingStudents():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917), Student(2, "Ale", 917), Student(3, "Mircea", 916)]
    assert service.filter_list_of_students_by_group(917) == 2
    assert len(service.list_of_students) == 1


def filterListOfStudentsByGroup_ANegativeGroup_ValueError():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917), Student(2, "Ale", 917), Student(3, "Mircea", 916)]
    try:
        x = service.filter_list_of_students_by_group(-1)
        assert x is None
        assert False
    except ValueError:
        assert True


def filterListOfStudentsByGroup_AGroupEqualTo0_ValueError():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917), Student(2, "Ale", 917), Student(3, "Mircea", 916)]
    try:
        x = service.filter_list_of_students_by_group(0)
        assert x is None
        assert False
    except ValueError:
        assert True


def filterListOfStudentsByGroup_AFloatInput_ValueError():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    try:
        service.filter_list_of_students_by_group(12.5)
        assert False
    except TypeError:
        assert True


def filterListOfStudentsByGroup_AStringInput_ValueError():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    try:
        service.filter_list_of_students_by_group("917")
        assert False
    except TypeError:
        assert True


def filterListOfStudentsByGroup_AListInput_ValueError():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    try:
        service.filter_list_of_students_by_group([917])
        assert False
    except TypeError:
        assert True


def filterListOfStudentsByGroup_ADictionaryInput_ValueError():
    service = Service()
    service.list_of_students = [Student(1, "Andrei", 917)]
    try:
        service.filter_list_of_students_by_group({"group": 917})
        assert False
    except TypeError:
        assert True


def test_filter_list_of_students_by_group():
    filterListOfStudentsByGroup_AGroupThatExistsInTheList_HowManyStudentsAreInThatGroupAndTheListWillModify()
    filterListOfStudentsByGroup_AGroupThatDoesNotExistInTheList_0AndTheListUnmodified()
    filterListOfStudentsByGroup_AGroupThatExistsInTheList_HowManyStudentsAreInThatGroupAndTheListWithTheRemainingStudents()
    filterListOfStudentsByGroup_ANegativeGroup_ValueError()
    filterListOfStudentsByGroup_AGroupEqualTo0_ValueError()
    filterListOfStudentsByGroup_AFloatInput_ValueError()
    filterListOfStudentsByGroup_AStringInput_ValueError()
    filterListOfStudentsByGroup_AListInput_ValueError()
    filterListOfStudentsByGroup_ADictionaryInput_ValueError()


def run_all_tests():
    test_add_student_to_list_of_students()
    test_filter_list_of_students_by_group()
