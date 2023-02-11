import unittest

from domain.question import Question
from repository.quiz_repository import QuizRepository
from controller.service import QuizService


class Testing(unittest.TestCase):
    def setUp(self) -> None:
        self.a_question = Question(1, "ABC", "A", "B", "C", "B", "easy")
        self.a_repository = QuizRepository("test.txt")
        self._service = QuizService("test.txt")

    def testQuestionDomain(self):
        self.assertEqual(self.a_question.question_id, 1)
        self.assertEqual(self.a_question.question_text, "ABC")
        self.assertEqual(self.a_question.answer1, "A")
        self.assertEqual(self.a_question.answer2, "B")
        self.assertEqual(self.a_question.answer3, "C")
        self.assertEqual(self.a_question.correct_answer, "B")
        self.assertEqual(self.a_question.difficulty, "easy")

    def testQuizRepository(self):
        self.assertIsInstance(self.a_repository.the_list_of_questions(), list)
        self.assertEqual(self.a_repository.number_of_questions(), len(self.a_repository.the_list_of_questions()))
        number_of_easy_questions = 0
        for question in self.a_repository.the_list_of_questions():
            if question.difficulty == "easy":
                number_of_easy_questions += 1
        self.assertEqual(self.a_repository.number_of_questions_from_given_difficulty("easy"), number_of_easy_questions)

    def testQuizService(self):
        with self.assertRaises(ValueError):
            self._service.add_question("1;2;3")
        with self.assertRaises(ValueError):
            self._service.create_quiz("hard", "1", "abc.txt")

    def tearDown(self) -> None:
        pass
