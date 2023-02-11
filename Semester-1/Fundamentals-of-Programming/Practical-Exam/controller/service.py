from repository.quiz_repository import QuizRepository
from domain.question import Question


class QuizService:
    def __init__(self, master_quiz_file_name):
        self._quiz_master_repository = QuizRepository(master_quiz_file_name)
        self._a_started_quiz_repository = None
        self._file_names_list = []

    def add_question(self, given_question):
        """ This function adds a question to the master quiz repository. """
        question_informations = given_question.split(";")
        if len(question_informations) != 7:
            raise ValueError("Invalid format for the question! ")
        question_id = int(question_informations[0].strip())
        question_text = question_informations[1].strip()
        answer1 = question_informations[2].strip()
        answer2 = question_informations[3].strip()
        answer3 = question_informations[4].strip()
        correct_answer = question_informations[5].strip()
        difficulty = question_informations[6].strip().lower()
        the_question = Question(question_id, question_text, answer1, answer2, answer3, correct_answer, difficulty)
        self._quiz_master_repository.add_question(the_question)

    def create_quiz(self, difficulty, number_of_questions, file_name):
        """ This function creates a new quiz with the given difficulty, number of questions and saves it in the given
        text file. """
        if difficulty.strip().lower() not in ("easy", "medium", "hard"):
            raise ValueError("Wrong input for difficulty!")
        if not number_of_questions.strip().isnumeric():
            raise ValueError("Number of questions should be a number!")
        if int(number_of_questions) > self._quiz_master_repository.number_of_questions():
            raise ValueError("There are not enough questions to create the quiz!")
        if int(number_of_questions) // 2 + 1 > self._quiz_master_repository.number_of_questions_from_given_difficulty(
                difficulty.strip().lower()):
            raise ValueError("There are not enough questions from given difficulty!")

        file = open(file_name, "w")
        quiz_questions = 0
        quiz_questions_list = []
        available_questions_list = self._quiz_master_repository.the_list_of_questions()
        for i in range(int(number_of_questions) // 2 + 1):
            quiz_questions += 1
            j = 0
            found = False
            while j < len(available_questions_list) and not found:
                question = available_questions_list[j]
                if question.difficulty == difficulty.strip().lower():
                    quiz_questions_list.append(question)
                    available_questions_list.pop(j)
                    found = True
                else:
                    j += 1
        while quiz_questions < int(number_of_questions):
            quiz_questions += 1
            j = 0
            found = False
            while j < len(available_questions_list) and not found:
                question = available_questions_list[j]
                if question.difficulty != difficulty.strip().lower():
                    quiz_questions_list.append(question)
                    available_questions_list.pop(j)
                    found = True
                else:
                    j += 1

        for question in quiz_questions_list:
            file.write(str(question) + "\n")
        file.close()

    def start_quiz(self, file_name):
        """ This function starts the quiz from the given text file name. """
        self._a_started_quiz_repository = QuizRepository(file_name)
        return self._a_started_quiz_repository.the_list_of_questions()
