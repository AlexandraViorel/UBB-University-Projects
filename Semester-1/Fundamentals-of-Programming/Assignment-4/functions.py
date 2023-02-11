"""
  Program functionalities module
"""


def get_expense_from_list(family_expenses_list, index):
    """
    This function returns the expense from the mentioned index
    :param family_expenses_list: the list of expenses
    :param index: the specified index
    :return: the expense from the specified index from the family expenses list
    """
    return family_expenses_list[index]


def test_get_expense_from_family_expenses_list():
    # This function tests the function named 'get_expense_from_family_expenses_list'.
    assert get_expense_from_list([[1, 20, "internet"], [1, 50, "food"]], 1) == [1, 50, "food"]


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
            create_expense(20, 300, "clothing"), create_expense(21, 45, "others"), create_expense(30, 60, "food"),
            create_expense(1, 800, "others"), create_expense(18, 5, "transport")]


def test_initialize_family_expenses_list():
    # This function tests the function named 'initialize_family_expenses_list'.
    assert initialize_family_expenses_list() == [[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"], [3, 15, "transport"], [20, 300, "clothing"],
                                                 [21, 45, "others"], [30, 60, "food"], [1, 800, "others"],
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
        if third_word_introduced == "to":
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
        if second_word_introduced == "day":
            return [first_word_introduced, second_word_introduced, None]
        else:
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


def calculate_category_sum(family_expenses_list, category):
    """
    This function calculates the sum of all expenses for a given category.
    :param family_expenses_list: the list with all expenses
    :param category: the given category to calculate the sum for
    :return: the sum of all expenses for the given category
    """
    given_category_sum = 0
    for expense in family_expenses_list:
        current_category = get_expense_category(expense)
        if category == current_category:
            current_amount_of_money = get_expense_amount_of_money(expense)
            given_category_sum = given_category_sum + current_amount_of_money
    return given_category_sum


def test_calculate_category_sum():
    # This function tests the function named 'calculate_category_sum'.
    assert calculate_category_sum([[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"]], "food") == 115


def calculate_total_amount_of_money_spent_on_a_given_day(family_expenses_list, day):
    """
    This function calculates the sum of all expenses for a given day.
    :param family_expenses_list: the list with all expenses
    :param day: the given day to calculate the sum for
    :return: the sum of all expenses for the given day
    """
    given_day_total_amount_of_money_spent = 0
    verify_day_parameter(day)
    for expense in family_expenses_list:
        current_day = get_expense_day(expense)
        if day == current_day:
            current_amount_of_money = get_expense_amount_of_money(expense)
            given_day_total_amount_of_money_spent = given_day_total_amount_of_money_spent + current_amount_of_money
    return given_day_total_amount_of_money_spent


def test_calculate_total_amount_of_money_spent_on_a_given_day():
    # This function tests the function named 'calculate_total_amount_of_money_spent_on_a_given_day'.
    assert calculate_total_amount_of_money_spent_on_a_given_day([[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"]], 3) == 176


def determine_the_day_with_maximum_expenses(family_expenses_list):
    """
    This function determines the day with the maximum amount of money spent.
    :param family_expenses_list: the list with all expenses
    :return: the day with the maximum amount of money spent
    """
    maximum_expenses = 0
    the_day_with_maximum_expenses = 0
    for day in range(1, 31):
        current_day_expenses = calculate_total_amount_of_money_spent_on_a_given_day(family_expenses_list, day)
        if current_day_expenses > maximum_expenses:
            maximum_expenses = current_day_expenses
            the_day_with_maximum_expenses = day
    return the_day_with_maximum_expenses


def test_determine_the_day_with_maximum_expenses():
    # This function tests the function named 'determine_the_day_with_maximum_expenses'.
    assert determine_the_day_with_maximum_expenses([[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"]]) == 3


def create_total_daily_expense(total_amount_of_money_spent, day):
    """
    This function creates the total daily expense.
    :param total_amount_of_money_spent: the total amount of money spent on that day
    :param day: the day
    :return: the total daily expense
    """
    verify_day_parameter(day)
    verify_amount_of_money_parameter(total_amount_of_money_spent)
    return [day, total_amount_of_money_spent]


def test_create_total_daily_expense():
    # This function tests the function named 'create_total_daily_expense'.
    assert create_total_daily_expense(800, 15) == [15, 800]


def get_total_amount_of_money_spent_on_a_day(total_daily_expense):
    """
    This function returns the total amount of money spent on a day.
    :param total_daily_expense:
    :return: the total amount of money
    """
    return total_daily_expense[1]


def test_get_total_amount_of_money_spent_on_a_day():
    # This function tests the function named 'get_total_amount_of_money_spent_on_a_day'.
    assert get_total_amount_of_money_spent_on_a_day([15, 800]) == 800


def create_list_with_total_amount_of_money_spent_on_days(family_expenses_list):
    """
    This function creates a list with the total amount of money spent on a day.
    :param family_expenses_list: the list with all expenses for each day
    :return: the list with the total amount of money for a day
    """
    total_amount_of_money_spent_on_days_list = []
    for day in range(1, 31):
        current_day_total_expenses = calculate_total_amount_of_money_spent_on_a_given_day(family_expenses_list, day)
        if current_day_total_expenses > 0:
            total_amount_of_money_spent_on_days_list.append(create_total_daily_expense(current_day_total_expenses, day))
    return total_amount_of_money_spent_on_days_list


def test_create_list_with_total_amount_of_money_spent_on_days():
    # This function tests the function named 'create_list_with_total_amount_of_money_spent_on_days'.
    assert create_list_with_total_amount_of_money_spent_on_days([[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"]]) == [[1, 15], [3, 176], [12, 50]]


def ascending_sort_by_total_amount_of_money_spent_on_days(total_amount_of_money_spent_on_days_list):
    # This function sorts the list ascending by the total amount of money spent on a day.
    for i in range(len(total_amount_of_money_spent_on_days_list) - 1):
        for j in range(i+1, len(total_amount_of_money_spent_on_days_list)):
            total_daily_expense_1 = get_expense_from_list(total_amount_of_money_spent_on_days_list, i)
            total_daily_expense_2 = get_expense_from_list(total_amount_of_money_spent_on_days_list, j)
            total_amount_of_money_spent_on_day_i = get_total_amount_of_money_spent_on_a_day(total_daily_expense_1)
            total_amount_of_money_spent_on_day_j = get_total_amount_of_money_spent_on_a_day(total_daily_expense_2)
            if total_amount_of_money_spent_on_day_i > total_amount_of_money_spent_on_day_j:
                total_amount_of_money_spent_on_days_list[i], total_amount_of_money_spent_on_days_list[j] = \
                    total_daily_expense_2, total_daily_expense_1


def create_list_with_expenses_from_given_category(family_expenses_list, category):
    """
    This function creates a list with all the expenses from a given category.
    :param family_expenses_list: the family expenses list
    :param category: the given category
    :return: the list with the expenses from the given category
    """
    expenses_from_given_category_list = []
    for expense in family_expenses_list:
        current_category = get_expense_category(expense)
        if current_category == category:
            day = get_expense_day(expense)
            amount_of_money = get_expense_amount_of_money(expense)
            expenses_from_given_category_list.append(create_expense(day, amount_of_money, category))
    return expenses_from_given_category_list


def test_create_list_with_expenses_from_given_category():
    # This function tests the function named 'create_list_with_expenses_from_given_category'.
    assert create_list_with_expenses_from_given_category([[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"], [3, 15, "transport"], [20, 300, "clothing"],
                                                 [21, 45, "others"], [30, 60, "food"], [1, 800, "others"],
                                                 [18, 5, "transport"]], "food") == [[1, 15, "food"], [3, 100, "food"],
                                                                                    [30, 60, "food"]]


def ascending_sort_by_amount_of_money_for_expenses_from_given_category(expenses_from_given_category_list):
    # This function sorts the list ascending by the amount of money for the list with the expenses
    # from a given category.
    for i in range(len(expenses_from_given_category_list) - 1):
        for j in range(i + 1, len(expenses_from_given_category_list)):
            expense_i = get_expense_from_list(expenses_from_given_category_list, i)
            expense_j = get_expense_from_list(expenses_from_given_category_list, j)
            amount_of_money_from_expense_i = get_expense_amount_of_money(expense_i)
            amount_of_money_from_expense_j = get_expense_amount_of_money(expense_j)
            if amount_of_money_from_expense_i > amount_of_money_from_expense_j:
                expenses_from_given_category_list[i], expenses_from_given_category_list[j] = expense_j, expense_i


def create_list_of_operations_that_modified_family_expenses_list():
    # This function initialize the list of operations that modified the family expenses list.
    return []


def create_list_of_versions_of_family_expenses_list():
    # This function initialize the list of versions of the family expenses list.
    return []


def copy_family_expenses_list(family_expenses_list):
    """
    This function makes a copy for the family expenses list.
    :param family_expenses_list: the list which will be copied
    :return: the copy of the list
    """
    copy_of_family_expenses_list = []
    for expense in family_expenses_list:
        copy_of_family_expenses_list.append(expense)
    return copy_of_family_expenses_list


def test_copy_family_expenses_list():
    # This function tests the function named 'copy_family_expenses_list'.
    assert copy_family_expenses_list([[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"], [3, 15, "transport"], [20, 300, "clothing"],
                                                 [21, 45, "others"], [30, 60, "food"], [1, 800, "others"],
                                                 [18, 5, "transport"]]) == [[1, 15, "food"], [12, 50, "internet"], [3, 100, "food"],
                                                 [3, 76, "housekeeping"], [3, 15, "transport"], [20, 300, "clothing"],
                                                 [21, 45, "others"], [30, 60, "food"], [1, 800, "others"],
                                                 [18, 5, "transport"]]


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
    test_copy_family_expenses_list()
    test_create_list_with_expenses_from_given_category()
    test_create_total_daily_expense()
    test_get_total_amount_of_money_spent_on_a_day()
    test_create_list_with_total_amount_of_money_spent_on_days()
    test_calculate_category_sum()
    test_calculate_total_amount_of_money_spent_on_a_given_day()
    test_determine_the_day_with_maximum_expenses()
