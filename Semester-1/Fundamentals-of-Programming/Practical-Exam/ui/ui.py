from controller.service import QuizService


class UI:
    def __init__(self, master_quiz_file_name):
        self._service = QuizService(master_quiz_file_name)

    def split_command(self, command):
        """ This functiion splits the command given by the user. """
        command = command.strip()
        command_list = command.split(" ")
        if command_list[0].strip().lower() == "add":
            if len(command_list) > 2:
                raise ValueError("Wrong command!")
            else:
                return command_list
        elif command_list[0].strip().lower() == "create":
            if len(command_list) > 4 :
                raise ValueError("Wrong command!")
            else:
                return command_list
        elif command_list[0].strip().lower() == "start":
            if len(command_list) > 2:
                raise ValueError("Wrong command!")
            else:
                return command_list
        elif command_list[0].strip().lower() == "exit":
            if len(command_list) > 1:
                raise ValueError("Wrong command!")
            else:
                return command_list
        else:
            raise ValueError("Wrong command!")

    def start_a_quiz(self, file_name):
        """ This function starts the quiz from the file given by the user. """
        print("The quiz starts: ")
        score = 0
        quiz_questions = self._service.start_quiz(file_name)
        for question in quiz_questions:
            print(question.question_text)
            print("1. " + question.answer1)
            print("2. " + question.answer2)
            print("3. " + question.answer3)
            choice = input("Write your option: ")
            while not choice.strip().isnumeric() or not choice.strip() in ("1", "2", "3"):
                print("Incorrect input. Try again!")
                choice = input("Write your option: ")
            if question.correct_answer == question.answer1 and int(choice.strip()) == 1:
                if question.difficulty == "easy":
                    score += 1
                elif question.difficulty == "medium":
                    score += 2
                else:
                    score += 3
            elif question.correct_answer == question.answer2 and int(choice.strip()) == 2:
                if question.difficulty == "easy":
                    score += 1
                elif question.difficulty == "medium":
                    score += 2
                else:
                    score += 3
            elif question.correct_answer == question.answer3 and int(choice.strip()) == 3:
                if question.difficulty == "easy":
                    score += 1
                elif question.difficulty == "medium":
                    score += 2
                else:
                    score += 3
        print("Your final score is : " + str(score))

    @staticmethod
    def print_options_menu():
        """ This function prints the possible commands. """
        print("You can choose between these commands:")
        print("add <id>;<text>;<choice_a>;<choice_b>;<choice_c>;<correct_choice>;<difficulty>")
        print("create <difficulty> <number_of_questions> <file>")
        print("start <file>")
        print("exit")

    def start_application(self):
        """ This function starts the application. """
        print("Welcome to quiz master !")

        while True:
            self.print_options_menu()
            command = input("Write your command> ")
            try:
                splitted_command = self.split_command(command)
                if splitted_command[0].strip().lower() == "add":
                    self._service.add_question(splitted_command[1].strip())
                elif splitted_command[0].strip().lower() == "create":
                    self._service.create_quiz(splitted_command[1].strip().lower(), splitted_command[2].strip().lower(),
                                              splitted_command[3].strip())
                elif splitted_command[0].strip().lower() == "start":
                    self.start_a_quiz(splitted_command[1].strip())
                elif splitted_command[0].strip().lower() == "exit":
                    return
                else:
                    raise Exception("Invalid command!")
            except Exception as message:
                print(str(message))

