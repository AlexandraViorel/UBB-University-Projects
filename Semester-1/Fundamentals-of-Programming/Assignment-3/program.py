"""
  Write non-UI functions below
"""


from datetime import date


def get_expense_from_family_expenses_list(family_expenses_list, index):
    """
    This function returns the expense from the mentioned index
    :param family_expenses_list: the list of expenses
    :param index: the specified index
    :return: the expense from the specified index from the family expenses list
    """
    return family_expenses_list[index]


def test_get_expense_from_family_expenses_list():
    # This function tests the function named 'get_expense_from_family_expenses_list'.
    assert get_expense_from_family_expenses_list([[1, 20, "internet"], [1, 50, "food"]], 1) == [1, 50, "food"]


def get_expense_day(expense):
    """
    This function returns the day of an expense.
    :param expense:
    :return: the day from the specified expense
    """
    return expense[0]


def test_get_expense_day():
    # This function tests the function named 'get_expense_day'.
    assert get_expense_day([15, 20, "internet"]) == 15


def get_expense_amount_of_money(expense):
    """
    This function returns the amount of money of an expense
    :param expense:
    :return: the amount of money from the specified expense
    """
    return expense[1]


def test_get_expense_amount_of_money():
    # This function tests the function named 'get_expense_amount_of_money'.
    assert get_expense_amount_of_money([15, 20, "internet"]) == 20


def get_expense_category(expense):
    """
    This function returns the category of an expense
    :param expense:
    :return: the category from specified expense
    """
    return expense[2]


def test_get_expense_category():
    # This function tests the function named 'get_expense_category'.
    assert get_expense_category([15, 20, "internet"]) == "internet"


def verify_category_parameter(category):
    # This function verifies if the category parameter is valid.
    categories_list = ["housekeeping", "food", "transport", "clothing", "internet", "others"]
    if category not in categories_list:
        raise ValueError("Invalid category !")


def verify_amount_of_money_parameter(amount_of_money):
    # This function verifies if the amount of money parameter is valid.
    if not isinstance(amount_of_money, int) or amount_of_money < 0:
        raise ValueError("Invalid type for amount of money!")


def verify_day_parameter(day):
    # This function verifies if the day parameter is valid.
    if not isinstance(day, int) or day < 1 or day > 30:
        raise ValueError("Invalid day !")


def create_expense(day, amount_of_money, category):
    """
    This function verifies the day, amount of money and category parameters and creates an expense.
    :param day: the given day
    :param amount_of_money: the given amount of money
    :param category: the given category
    :return: the expense
    """
    verify_category_parameter(category)
    verify_day_parameter(day)
    verify_amount_of_money_parameter(amount_of_money)
    return [int(day), int(amount_of_money), category.lower()]


def test_create_expense():
    # This function tests the function named 'create_expense'.
    assert create_expense(15, 20, "internet") == [15, 20, 'internet']


def find_expense_at_some_day_and_some_category(family_expenses_list, day, category):
    """
    This function searches if there exists an expense at a given day and a given category.
    :param family_expenses_list:
    :param day: the day we search expense at
    :param category: the category we search expense at
    :return: the index if it finds an expense, else it returns the string: "specified category not found at specified
    day"
    """
    verify_day_parameter(day)
    verify_category_parameter(category)
    index = 0
    for expense in family_expenses_list:
        auxiliary_day = get_expense_day(expense)
        auxiliary_category = get_expense_category(expense)
        if auxiliary_day == int(day) and auxiliary_category == category.lower():
            return index
        index += 1
    if index == len(family_expenses_list):
        return "specified category not found at specified day"


def test_find_expense_at_some_day_and_some_category():
    # This function tests the function named 'find_expense_at_some_day_and_some_category'.
    assert find_expense_at_some_day_and_some_category([[1, 20, "internet"], [1, 50, "food"]], 1, "food") == 1
    assert find_expense_at_some_day_and_some_category([[1, 20, "internet"],
                                                       [1, 50, "food"]], 2, "food") == "specified " \
                                                                                       "category not found at " \
                                                                                       "specified day"


def verify_if_day_exists_in_family_expenses_list(family_expenses_list, day):
    """
    This function searches if there exists an expense at a given day.
    :param family_expenses_list:
    :param day: the day we search expense at
    :return: the string: "specified day does not exist in family expenses list" if it does not find an expense at the
    specified day, else the string: "specified day exists in family expenses list"
    """
    verify_day_parameter(day)
    day_exists = 0
    for expense in family_expenses_list:
        auxiliary_day = get_expense_day(expense)
        if auxiliary_day == int(day):
            day_exists += 1
    if day_exists == 0:
        return "specified day does not exist in family expenses list"
    else:
        return "specified day exists in family expenses list"


def test_verify_if_day_exists_in_family_expenses_list():
    # This function tests the function named 'verify_if_day_exists_in_family_expenses_list'.
    assert verify_if_day_exists_in_family_expenses_list([[1, 20, "internet"],
                                                         [1, 50, "food"]], 1) == "specified day exists in family " \
                                                                                 "expenses list"
    assert verify_if_day_exists_in_family_expenses_list([[1, 20, "internet"],
                                                         [1, 50, "food"]], 2) == "specified day does not exist in " \
                                                                                 "family expenses list"


def verify_if_category_exists_in_family_expenses_list(family_expenses_list, category):
    """
    This function searches if there exists an expense from a given category.
    :param family_expenses_list:
    :param category: the category from which we search expenses
    :return: the string: 'specified category does not exist in family expenses list' if it does not find an expense from
    the specified category, else the string: 'specified category exists in family expenses list'
    """
    verify_category_parameter(category)
    category_exists = 0
    for expense in family_expenses_list:
        auxiliary_category = get_expense_category(expense)
        if auxiliary_category == category.lower():
            category_exists += 1
    if category_exists == 0:
        return "specified category does not exist in family expenses list"
    else:
        return "specified category exists in family expenses list"


def test_verify_if_category_exists_in_family_expenses_list():
    # This function tests the function named 'verify_if_category_exists_in_family_expenses_list'.
    assert verify_if_category_exists_in_family_expenses_list([[1, 20, "internet"],
                                                              [1, 50, "food"]], "food") == "specified category " \
                                                                                           "exists in family " \
                                                                                           "expenses list"
    assert verify_if_category_exists_in_family_expenses_list([[1, 20, "internet"],
                                                              [1, 50, "food"]],
                                                             "housekeeping") == "specified category does not exist " \
                                                                                "in family expenses list"


def initialize_family_expenses_list():
    """
    This function creates a list with 10 expenses
    :return: the list of expenses
    """
    return [create_expense(1, 15, "food"), create_expense(12, 50, "internet"), create_expense(3, 100, "food"),
            create_expense(3, 76, "housekeeping"), create_expense(3, 15, "transport"),
            create_expense(20, 300, "clothing"), create_expense(21, 45, "others"), create_expense(29, 60, "food"),
            create_expense(1, 800, "others"), create_expense(18, 5, "transport")]


def test_initialize_family_expenses_list():
    assert initialize_family_expenses_list() == [[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"], [3, 15, "transport"], [20, 300, "clothing"],
                                                 [21, 45, "others"], [29, 60, "food"], [1, 800, "others"],
                                                 [18, 5, "transport"]]


def split_command(command):
    """
    This function divides the user command into command words and command parameters.
    :param command: user command
    :return: a list with the command words and the command parameters
    """
    command = command.strip()
    splitted_command_list = command.split(sep=" ")
    index = 0
    while index < len(splitted_command_list):
        if splitted_command_list[index] == "":
            splitted_command_list.pop(index)
        else:
            index += 1
    if len(splitted_command_list) == 4:
        first_word_introduced = splitted_command_list[0].strip().lower()
        second_word_introduced = splitted_command_list[1].strip().lower()
        third_word_introduced = splitted_command_list[2].strip().lower()
        fourth_word_introduced = splitted_command_list[3].strip().lower()
        if ("to" in splitted_command_list) or ("tO" in splitted_command_list) or ("TO" in splitted_command_list) or \
                ("To" in splitted_command_list):
            return [first_word_introduced, third_word_introduced,
                    second_word_introduced + "," + fourth_word_introduced]
        elif ("<" in splitted_command_list) or ("=" in splitted_command_list) or (">" in splitted_command_list):
            return [first_word_introduced, third_word_introduced,
                    second_word_introduced + "," + fourth_word_introduced]
        else:
            return [first_word_introduced, None,
                    second_word_introduced + "," + third_word_introduced +
                    "," + fourth_word_introduced]
    elif len(splitted_command_list) == 3:
        first_word_introduced = splitted_command_list[0].strip().lower()
        second_word_introduced = splitted_command_list[1].strip().lower()
        third_word_introduced = splitted_command_list[2].strip().lower()
        return [first_word_introduced, None, second_word_introduced + "," +
                third_word_introduced]
    elif len(splitted_command_list) == 2:
        first_word_introduced = splitted_command_list[0].strip().lower()
        second_word_introduced = splitted_command_list[1].strip().lower()
        return [first_word_introduced, None, second_word_introduced]
    elif len(splitted_command_list) == 1:
        first_word_introduced = splitted_command_list[0].strip().lower()
        return [first_word_introduced, None, None]
    else:
        return [None, None, None]


def test_split_command():
    # This function tests the function named 'split_command'.
    assert split_command("add 10 internet") == ["add", None, "10,internet"]
    assert split_command("ADD 10 intERNET") == ["add", None, "10,internet"]
    assert split_command("insert 25 100 food") == ["insert", None, "25,100,food"]
    assert split_command("remove 15") == ["remove", None, "15"]
    assert split_command("remove 1 to 3") == ["remove", "to", "1,3"]
    assert split_command("remove 1 TO 3") == ["remove", "to", "1,3"]
    assert split_command("remove food") == ["remove", None, "food"]
    assert split_command("list") == ["list", None, None]
    assert split_command("list food") == ["list", None, "food"]
    assert split_command("list food > 5") == ["list", ">", "food,5"]
    assert split_command("exit") == ["exit", None, None]
    assert split_command("") == [None, None, None]


def split_parameters(command_parameters):
    """
    This function divides the command parameters.
    :param command_parameters:
    :return: the list with the parameters
    """
    if command_parameters is None:
        raise ValueError("Parameters does not exist !")
    else:
        splitted_parameters_list = command_parameters.split(",")
        parameters_list = []
        if len(splitted_parameters_list) == 1:
            first_parameter = splitted_parameters_list[0].strip().lower()
            if first_parameter.isnumeric():
                parameters_list.append(int(first_parameter))
            else:
                parameters_list.append(first_parameter)
        elif len(splitted_parameters_list) == 2:
            first_parameter = splitted_parameters_list[0].strip().lower()
            second_parameter = splitted_parameters_list[1].strip().lower()
            if first_parameter.isnumeric():
                parameters_list.append(int(first_parameter))
            else:
                parameters_list.append(first_parameter)
            if second_parameter.isnumeric():
                parameters_list.append(int(second_parameter))
            else:
                parameters_list.append(second_parameter)
        elif len(splitted_parameters_list) == 3:
            first_parameter = splitted_parameters_list[0].strip().lower()
            second_parameter = splitted_parameters_list[1].strip().lower()
            third_parameter = splitted_parameters_list[2].strip().lower()
            parameters_list.append(int(first_parameter))
            parameters_list.append(int(second_parameter))
            parameters_list.append(third_parameter)
        else:
            raise ValueError("Invalid parameters !")
        return parameters_list


def test_split_parameters():
    # This function tests the function named 'split_parameters'.
    assert split_parameters("10,internet") == [10, "internet"]
    assert split_parameters("internet,10") == ["internet", 10]
    assert split_parameters("1,3") == [1, 3]
    assert split_parameters("25,100,food") == [25, 100, "food"]
    assert split_parameters("food") == ["food"]
    assert split_parameters("1") == [1]


def verify_one_command_parameter(command_parameters):
    """
    This function tests which kind of parameter is the command parameter.
    :param command_parameters:
    :return: the string 'a day' if the command parameter is a day, 'a category' if the command parameter is a expense
    category and 'wrong' if isn't a day or a category
    """
    categories_list = ["housekeeping", "food", "transport", "clothing", "internet", "others"]
    parameters_test_list = split_parameters(command_parameters)
    if len(parameters_test_list) > 1 or len(parameters_test_list) == 0:
        return "wrong"
    elif parameters_test_list[0] in categories_list:
        return "a category"
    elif isinstance(parameters_test_list[0], int) and 1 <= parameters_test_list[0] <= 30:
        return "a day"
    else:
        raise ValueError("Invalid parameter !")


def test_verify_one_command_parameter():
    # This function tests the function named 'verify_one_command_parameter'.
    assert verify_one_command_parameter("15") == "a day"
    assert verify_one_command_parameter("15,food") == "wrong"
    assert verify_one_command_parameter("food") == "a category"


# Here are all the tests !
def run_all_tests():
    test_get_expense_from_family_expenses_list()
    test_get_expense_day()
    test_get_expense_amount_of_money()
    test_get_expense_category()
    test_create_expense()
    test_find_expense_at_some_day_and_some_category()
    test_verify_if_day_exists_in_family_expenses_list()
    test_verify_if_category_exists_in_family_expenses_list()
    test_initialize_family_expenses_list()
    test_split_command()
    test_split_parameters()
    test_verify_one_command_parameter()


"""
  Write the command-driven UI below
"""


def add_expenses_to_current_day(family_expenses_list, command_parameters):
    # This function adds an expense to the current day.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 2:
        raise ValueError("Number of parameters is not correct !")
    else:
        amount_of_money = parameters_list[0]
        verify_amount_of_money_parameter(amount_of_money)
        category = parameters_list[1]
        verify_category_parameter(category)
        today = str(date.today())
        today_day = int(str(today[len(today) - 2]) + str(today[len(today) - 1]))
        if find_expense_at_some_day_and_some_category(family_expenses_list, today_day,
                                                      category) != "specified category not found at specified day":
            index = find_expense_at_some_day_and_some_category(family_expenses_list, today_day, category)
            family_expenses_list[index][1] = family_expenses_list[index][1] + amount_of_money
            # only amount of money changes
        else:
            family_expenses_list.append(create_expense(today_day, amount_of_money, category))
        print("Expense added successfully !")


def insert_expenses_to_chosen_day(family_expenses_list, command_parameters):
    # This function inserts to a given day an expense.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 3:
        raise ValueError("Number of parameters is not correct !")
    else:
        day = get_expense_day(parameters_list)
        amount_of_money = get_expense_amount_of_money(parameters_list)
        category = get_expense_category(parameters_list)
        if find_expense_at_some_day_and_some_category(family_expenses_list, day,
                                                      category) != "specified category not found at specified day":
            index = find_expense_at_some_day_and_some_category(family_expenses_list, day, category)
            verify_amount_of_money_parameter(amount_of_money)
            family_expenses_list[index][1] = family_expenses_list[index][1] + amount_of_money
            # only amount of money changes
            print("Expense added successfully !")
        else:
            family_expenses_list.append(create_expense(day, amount_of_money, category))
            print("Expense added successfully !")


def remove_expenses_from_specified_day(family_expenses_list, command_parameters):
    # This function removes all expenses from a given day.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 1:
        raise ValueError("Number of parameters is not correct !")
    else:
        day = parameters_list[0]
        verify_day_parameter(day)
        index = 0
        if verify_if_day_exists_in_family_expenses_list(family_expenses_list,
                                                        day) == "specified day does not exist in family expenses list":
            print("There are no expenses in the specified day !")
        else:
            while index < len(family_expenses_list):
                expense = get_expense_from_family_expenses_list(family_expenses_list, index)
                auxiliary_day = get_expense_day(expense)
                if auxiliary_day == int(day):
                    family_expenses_list.pop(index)
                    print("Expenses removed successfully !")
                else:
                    index += 1


def remove_expenses_from_specified_category(family_expenses_list, command_parameters):
    # This function removes all expenses from a given category.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 1:
        raise ValueError("Number of parameters is not correct !")
    else:
        category = parameters_list[0]
        verify_category_parameter(category)
        index = 0
        if verify_if_category_exists_in_family_expenses_list(family_expenses_list,
                                                             category) == "specified category does not exist in " \
                                                                          "family expenses list":
            print("There are no expenses from specified category !")
        else:
            while index < len(family_expenses_list):
                expense = get_expense_from_family_expenses_list(family_expenses_list, index)
                auxiliary_category = get_expense_category(expense)
                if auxiliary_category == category:
                    family_expenses_list.pop(index)
                    print("Expenses removed successfully !")
                else:
                    index += 1


def remove_expenses_from_day1_to_day2(family_expenses_list, command_parameters):
    # This function removes all expenses from day1 to day 2.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 2:
        raise ValueError("Number of parameters is not correct !")
    else:
        start_day = parameters_list[0]
        verify_day_parameter(start_day)
        end_day = parameters_list[1]
        verify_day_parameter(end_day)
        if int(start_day) > int(end_day):
            raise ValueError("Start day cannot be greater than end day !")
        else:
            index = 0
            how_many_days = end_day - start_day + 1
            count = 0
            for i in range(start_day, end_day+1):
                if verify_if_day_exists_in_family_expenses_list(family_expenses_list, i) == "specified day does not " \
                                                                                            "exist in family " \
                                                                                            "expenses list":
                    count += 1
            if how_many_days == count:
                print("There are no expenses in these days !")
            else:
                while index < len(family_expenses_list):
                    expense = get_expense_from_family_expenses_list(family_expenses_list, index)
                    auxiliary_day = get_expense_day(expense)
                    if int(start_day) <= auxiliary_day <= int(end_day):
                        family_expenses_list.pop(index)
                    else:
                        index += 1
                print("Expenses removed successfully !")


def display_expense(expense, index):
    # This function prints an expense.
    day = str(get_expense_day(expense))
    amount_of_money = str(get_expense_amount_of_money(expense))
    category = str(get_expense_category(expense))
    print(str(index) + " : day " + day + ", amount of money: " + amount_of_money + "LEI, category: " + category)


def display_entire_expenses_list(family_expenses_list):
    # This function prints all expenses from the family expenses list.
    if len(family_expenses_list) == 0:
        print("The family expenses list is empty !")
    else:
        index = 1
        for expense in family_expenses_list:
            day = str(get_expense_day(expense))
            amount_of_money = str(get_expense_amount_of_money(expense))
            category = str(get_expense_category(expense))
            print(str(index) + " : day " + day + ", amount of money: " + amount_of_money + "LEI, category: " + category)
            index += 1


def display_expenses_from_specified_category(family_expenses_list, command_parameters):
    # This function prints the expenses from a given category.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 1:
        raise ValueError("Number of parameters is not correct")
    else:
        category = parameters_list[0]
        verify_category_parameter(category)
        if verify_if_category_exists_in_family_expenses_list(family_expenses_list,
                                                             category) == "specified category does not exist in " \
                                                                          "family expenses list":
            print("There are no expenses from specified category !")
        index = 1
        for expense in family_expenses_list:
            auxiliary_category = get_expense_category(expense)
            if auxiliary_category == category:
                display_expense(expense, index)
                index += 1


def display_expenses_from_specified_category_and_specified_amount_of_money(family_expenses_list, command_parameters,
                                                                           command_word):
    # This function prints the expenses from a given category and a given amount of money.
    parameters_list = split_parameters(command_parameters)
    sign = command_word
    if len(parameters_list) != 2:
        raise ValueError("Number of parameters is not correct")
    else:
        category = parameters_list[0]
        verify_category_parameter(category)
        value = parameters_list[1]
        verify_amount_of_money_parameter(value)
        index = 1
        for expense in family_expenses_list:
            auxiliary_category = get_expense_category(expense)
            auxiliary_amount_of_money = get_expense_amount_of_money(expense)
            if auxiliary_category == category:
                if sign == ">":
                    if auxiliary_amount_of_money > value:
                        display_expense(expense, index)
                        index += 1
                elif sign == "=":
                    if auxiliary_amount_of_money == value:
                        display_expense(expense, index)
                        index += 1
                else:
                    if auxiliary_amount_of_money < value:
                        display_expense(expense, index)
                        index += 1


def start_command():
    run_all_tests()
    family_expenses_list = initialize_family_expenses_list()

    while True:
        command = input("prompt> ")
        command_word1, command_word2, command_parameters = split_command(command)

        try:
            if command_word1 == "add" and command_word2 is None:
                add_expenses_to_current_day(family_expenses_list, command_parameters)
            elif command_word1 == "insert" and command_word2 is None:
                insert_expenses_to_chosen_day(family_expenses_list, command_parameters)
            elif command_word1 == "remove" and command_word2 is None:
                if verify_one_command_parameter(command_parameters) == "a day":
                    remove_expenses_from_specified_day(family_expenses_list, command_parameters)
                elif verify_one_command_parameter(command_parameters) == "a category":
                    remove_expenses_from_specified_category(family_expenses_list, command_parameters)
                else:
                    print("Invalid parameters !")
            elif command_word1 == "remove" and command_word2 == "to":
                remove_expenses_from_day1_to_day2(family_expenses_list, command_parameters)
            elif command_word1 == "list" and command_word2 is None:
                if command_parameters is None:
                    display_entire_expenses_list(family_expenses_list)
                elif verify_one_command_parameter(command_parameters) == "a category":
                    display_expenses_from_specified_category(family_expenses_list, command_parameters)
                else:
                    print("Invalid parameters !")
            elif command_word1 == "list" and command_word2 in ["<", "=", ">"]:
                display_expenses_from_specified_category_and_specified_amount_of_money(family_expenses_list,
                                                                                       command_parameters,
                                                                                       command_word2)
            elif command_word1 == "exit" and command_word2 is None and command_parameters is None:
                return
            else:
                print("Command does not exist !")
        except ValueError as value_error_var:
            print(str(value_error_var))


start_command()
