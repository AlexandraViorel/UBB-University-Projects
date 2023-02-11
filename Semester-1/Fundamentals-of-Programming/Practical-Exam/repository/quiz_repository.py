from domain.question import Question


class QuizRepository:
    def __init__(self, file_name):
        self._questions_list = list()
        self._file_name = file_name
        self._load_file()

    def the_list_of_questions(self):
        """ This fuinction returns the list of questions from the repository"""
        return self._questions_list

    def _load_file(self):
        """ This function loads the questions from the text file into the repository. """
        try:
            file = open(self._file_name, "r")
        except IOError:
            raise Exception("The file does not exist!")
        line = file.readline()
        while line != "":
            question_informations = line.split(";")
            question_id = int(question_informations[0].strip())
            question_text = question_informations[1].strip()
            answer1 = question_informations[2].strip()
            answer2 = question_informations[3].strip()
            answer3 = question_informations[4].strip()
            correct_answer = question_informations[5].strip()
            difficulty = question_informations[6].strip().lower()
            the_question = Question(question_id, question_text, answer1, answer2, answer3, correct_answer, difficulty)
            self._questions_list.append(the_question)
            line = file.readline()

        file.close()

    def _save_file(self):
        """ This function saves the questions from the repository into a text file. """
        file = open(self._file_name, "w")
        for question in self._questions_list:
            file.write(str(question) + "\n")
        file.close()

    def number_of_questions(self):
        """ This function returns the number of questions we have in the repository. """
        return len(self._questions_list)

    def number_of_questions_from_given_difficulty(self, given_difficulty):
        """ This function returns how many questions with a given difficulty we have in the repository"""
        number_of_questions = 0
        for question in self._questions_list:
            if question.difficulty == given_difficulty:
                number_of_questions += 1
        return number_of_questions

    def add_question(self, question):
        """ This function adds a new question to the repository and writes it in the text file. """
        self._questions_list.append(question)
        self._save_file()
