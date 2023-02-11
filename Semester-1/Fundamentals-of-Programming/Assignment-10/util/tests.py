import unittest
from src.util.util import *


class TestUtil(unittest.TestCase):
    def setUp(self) -> None:
        self.container = MyContainer()

    def test_setitem__theKeyAndTheValue__theElementAddedToTheContainer(self):
        self.container.__setitem__(1, "abc")
        self.assertEqual(len(self.container), 1)

    def test_getitem__theKeyOfTheItemWeWant__theElementThatWeWant(self):
        self.container.add(1, "abc")
        self.assertEqual(self.container.__getitem__(1), "abc")

    def test_delitem__theKeyOfTheItemWeWantToDelete__theElementDeleted(self):
        self.container.add(1, "abc")
        self.container.__delitem__(1)
        self.assertEqual(len(self.container), 0)

    def test_len__noInput__theLengthOfTheDictionary(self):
        self.assertEqual(self.container.__len__(), 0)

    def test_list__noInput__listOfTheValuesOfTheDictionaryElements(self):
        self.container.add(1, "abc")
        self.assertEqual(self.container.list(), ["abc"])

    def test_iter__NoInput__zero(self):
        self.assertEqual(self.container.__iter__(), 0)

    def test_next__NoInput__StopIterationWhenPassesThroughAllTheElementsFromTheDictionary(self):
        self.container.add(1, "abc")
        self.container.add(2, "abc")
        self.container.__iter__()
        self.container.__next__()
        self.container.__next__()
        with self.assertRaises(StopIteration):
            self.container.__next__()

    def test_add__theKeyAndTheElement__theElementAddedToTheDictionary(self):
        self.container.add(1, "abc")
        self.assertEqual(len(self.container), 1)

    def test_remove__theKeyOfTheElementWeWantToRemove__theElementRemovedFromTheDictionary(self):
        self.container.add(1, "abc")
        self.container.remove(1)
        self.assertEqual(len(self.container), 0)

    def test_update__theKeyAndTheNewElement__theDictionaryWithTheElementUpdated(self):
        self.container.add(1, "abc")
        self.container.update(1, "abcdef")
        self.assertEqual(self.container[1], "abcdef")

    def test_myShellSort__theListToBeSortedAndTheComparisonFunction__TheSortedList(self):
        def comparison_function(a, b):
            return a > b
        the_list_to_be_sorted = [9, 8, 3, 7, 5, 6, 4, 1, 2]
        self.assertEqual(my_shell_sort(the_list_to_be_sorted, comparison_function), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_myFilter__theListToBeFilteredAndTheFilterFunction__TheFilteredList(self):
        def filter_function(a):
            return a < 5
        the_list_to_be_filtered = [9, 8, 3, 7, 5, 6, 4, 1, 2]
        self.assertEqual(my_filter(the_list_to_be_filtered, filter_function), [3, 4, 1, 2])

    def tearDown(self) -> None:
        pass
