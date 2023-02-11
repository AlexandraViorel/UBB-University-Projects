class Question:
    """ This class stores all informations about a question. """
    def __init__(self, question_id, question_text, answer1, answer2, answer3, correct_answer, difficulty):
        self._question_id = question_id
        self._question_text = question_text
        self._answer1 = answer1
        self._answer2 = answer2
        self._answer3 = answer3
        self._correct_answer = correct_answer
        self._difficulty = difficulty

    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        self._question_id = question_id

    @property
    def question_text(self):
        return self._question_text

    @question_text.setter
    def question_text(self, question_text):
        self._question_text = question_text

    @property
    def answer1(self):
        return self._answer1

    @answer1.setter
    def answer1(self, answer1):
        self._answer1 = answer1

    @property
    def answer2(self):
        return self._answer2

    @answer2.setter
    def answer2(self, answer2):
        self._answer2 = answer2

    @property
    def answer3(self):
        return self._answer3

    @answer3.setter
    def answer3(self, answer3):
        self._answer3 = answer3

    @property
    def correct_answer(self):
        return self._correct_answer

    @correct_answer.setter
    def correct_answer(self, correct_answer):
        self._correct_answer = correct_answer

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty

    def __str__(self):
        return str(self._question_id) + ";" + str(self._question_text) + ";" + str(self._answer1) + ";" + \
               str(self._answer2) + ";" + str(self._answer3) + ";" + str(self._correct_answer) + ";" + \
               str(self._difficulty)
