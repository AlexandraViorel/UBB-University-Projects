"""
  User interface module
"""


from datetime import date
from functions import *


def add_expenses_to_current_day(family_expenses_list, command_parameters,
                                list_of_operations_that_modified_family_expenses_list,
                                list_of_versions_of_family_expenses_list):
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

        copy_of_family_expenses_list = copy_family_expenses_list(family_expenses_list)
        list_of_versions_of_family_expenses_list.append(copy_of_family_expenses_list)

        if find_expense_at_some_day_and_some_category(family_expenses_list, today_day,
                                                      category) != "specified category not found at specified day":
            index = find_expense_at_some_day_and_some_category(family_expenses_list, today_day, category)
            family_expenses_list[index][1] = family_expenses_list[index][1] + amount_of_money
            # only amount of money changes

        else:
            family_expenses_list.append(create_expense(today_day, amount_of_money, category))

        print("Expense added successfully !")

        list_of_operations_that_modified_family_expenses_list.append("add " + str(amount_of_money) + " " + category)


def insert_expenses_to_chosen_day(family_expenses_list, command_parameters,
                                  list_of_operations_that_modified_family_expenses_list,
                                  list_of_versions_of_family_expenses_list):
    # This function inserts to a given day an expense.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 3:
        raise ValueError("Number of parameters is not correct !")

    else:
        day = get_expense_day(parameters_list)
        verify_day_parameter(day)

        amount_of_money = get_expense_amount_of_money(parameters_list)
        verify_amount_of_money_parameter(amount_of_money)

        category = get_expense_category(parameters_list)
        verify_category_parameter(category)

        copy_of_family_expenses_list = copy_family_expenses_list(family_expenses_list)
        list_of_versions_of_family_expenses_list.append(copy_of_family_expenses_list)

        if find_expense_at_some_day_and_some_category(family_expenses_list, day,
                                                      category) != "specified category not found at specified day":
            index = find_expense_at_some_day_and_some_category(family_expenses_list, day, category)
            family_expenses_list[index][1] = family_expenses_list[index][1] + amount_of_money
            # only amount of money changes
            print("Expense added successfully !")

        else:
            family_expenses_list.append(create_expense(day, amount_of_money, category))
            print("Expense added successfully !")

        list_of_operations_that_modified_family_expenses_list.append("insert " + str(day) + " " + str(amount_of_money) +
                                                                     " " + category)


def remove_expenses_from_specified_day(family_expenses_list, command_parameters,
                                       list_of_operations_that_modified_family_expenses_list,
                                       list_of_versions_of_family_expenses_list):
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
            copy_of_family_expenses_list = copy_family_expenses_list(family_expenses_list)
            list_of_versions_of_family_expenses_list.append(copy_of_family_expenses_list)

            while index < len(family_expenses_list):
                expense = get_expense_from_list(family_expenses_list, index)
                auxiliary_day = get_expense_day(expense)

                if auxiliary_day == int(day):
                    family_expenses_list.pop(index)
                    print("Expenses removed successfully !")

                else:
                    index += 1

            list_of_operations_that_modified_family_expenses_list.append("remove " + str(day))


def remove_expenses_from_specified_category(family_expenses_list, command_parameters,
                                            list_of_operations_that_modified_family_expenses_list,
                                            list_of_versions_of_family_expenses_list):
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
            copy_of_family_expenses_list = copy_family_expenses_list(family_expenses_list)
            list_of_versions_of_family_expenses_list.append(copy_of_family_expenses_list)
            while index < len(family_expenses_list):
                expense = get_expense_from_list(family_expenses_list, index)
                auxiliary_category = get_expense_category(expense)
                if auxiliary_category == category:
                    family_expenses_list.pop(index)
                    print("Expenses removed successfully !")
                else:
                    index += 1
            list_of_operations_that_modified_family_expenses_list.append("remove " + category)


def remove_expenses_from_day1_to_day2(family_expenses_list, command_parameters,
                                      list_of_operations_that_modified_family_expenses_list,
                                      list_of_versions_of_family_expenses_list):
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
                copy_of_family_expenses_list = copy_family_expenses_list(family_expenses_list)
                list_of_versions_of_family_expenses_list.append(copy_of_family_expenses_list)
                while index < len(family_expenses_list):
                    expense = get_expense_from_list(family_expenses_list, index)
                    auxiliary_day = get_expense_day(expense)
                    if int(start_day) <= auxiliary_day <= int(end_day):
                        family_expenses_list.pop(index)
                    else:
                        index += 1
                print("Expenses removed successfully !")
                list_of_operations_that_modified_family_expenses_list.append("remove " + str(start_day) + " to " +
                                                                             str(end_day))


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


def display_category_sum(family_expenses_list, command_parameters):
    # This function prints the total amount of money spent from the given category.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 1:
        raise ValueError("Number of parameters is not correct !")
    else:
        category = parameters_list[0]
        verify_category_parameter(category)
        given_category_sum = calculate_category_sum(family_expenses_list, category)
        print("The total amount of money spent from the category " + category + " is: " + str(given_category_sum) + " LEI")


def display_the_day_with_maximum_expenses(family_expenses_list, command_parameters):
    # This function prints the day with the maximum amount of money spent.
    if command_parameters is not None:
        raise ValueError("This option cannot have parameters !")
    else:
        the_day_with_maximum_expenses = determine_the_day_with_maximum_expenses(family_expenses_list)
        print("The day with the maximum expenses is: " + str(the_day_with_maximum_expenses))


def display_total_daily_expense(daily_expense, index):
    # This function prints an total daily expense.
    day = str(get_expense_day(daily_expense))
    total_amount_of_money = str(get_total_amount_of_money_spent_on_a_day(daily_expense))
    print(str(index) + " : day " + day + ", total amount of money spent: " + total_amount_of_money + " LEI")


def display_total_daily_expenses_in_ascending_order_by_amount_of_money_spent(family_expenses_list, command_parameters):
    # This function prints the list of total daily expenses in ascending order by amount of money spent.
    if command_parameters is not None:
        raise ValueError("This option cannot have parameters !")
    else:
        total_amount_of_money_spent_on_days_list = create_list_with_total_amount_of_money_spent_on_days(
            family_expenses_list)
        ascending_sort_by_total_amount_of_money_spent_on_days(total_amount_of_money_spent_on_days_list)
        index = 1
        for daily_expense in total_amount_of_money_spent_on_days_list:
            display_total_daily_expense(daily_expense, index)
            index += 1


def display_expenses_for_given_category_in_ascending_order_by_amount_of_money_spent(family_expenses_list,
                                                                                    command_parameters):
    # This function prints the expenses from a given category in ascending order by the amount of money spent.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 1:
        raise ValueError("Invalid number of parameters !")
    else:
        category = parameters_list[0]
        verify_category_parameter(category)
        expenses_from_given_category_list = create_list_with_expenses_from_given_category(family_expenses_list,
                                                                                          category)
        ascending_sort_by_amount_of_money_for_expenses_from_given_category(expenses_from_given_category_list)
        index = 1
        for expense in expenses_from_given_category_list:
            display_expense(expense, index)
            index += 1


def filter_by_given_category(family_expenses_list, command_parameters,
                             list_of_operations_that_modified_family_expenses_list,
                             list_of_versions_of_family_expenses_list):
    # This function keeps only the expenses from the given category in the family expenses list and deletes all other
    # expenses.
    parameters_list = split_parameters(command_parameters)
    if len(parameters_list) != 1:
        raise ValueError("Invalid number of parameters !")
    else:
        given_category = parameters_list[0]
        verify_category_parameter(given_category)
        index = 0
        copy_of_family_expenses_list = copy_family_expenses_list(family_expenses_list)
        list_of_versions_of_family_expenses_list.append(copy_of_family_expenses_list)
        while index < len(family_expenses_list):
            current_expense = get_expense_from_list(family_expenses_list, index)
            current_category = get_expense_category(current_expense)
            if current_category != given_category:
                family_expenses_list.pop(index)
            else:
                index += 1
        if len(family_expenses_list) == 0:
            print("There were no expenses from " + given_category + " category, so all expenses were removed from list !")
        else:
            print("List was filtered successfully !")
        list_of_operations_that_modified_family_expenses_list.append("filter " + given_category)


def filter_by_given_category_and_given_amount_of_money_range(family_expenses_list, command_parameters, command_word,
                                                             list_of_operations_that_modified_family_expenses_list,
                                                             list_of_versions_of_family_expenses_list):
    # This function keeps only the expenses from the given category and given amount of money range and deletes all
    # other expenses.
    parameters_list = split_parameters(command_parameters)
    sign = command_word
    if len(parameters_list) != 2:
        raise ValueError("Invalid number of parameters !")
    else:
        given_category = parameters_list[0]
        verify_category_parameter(given_category)
        given_amount_of_money = parameters_list[1]
        verify_amount_of_money_parameter(given_amount_of_money)
        index = 0
        copy_of_family_expenses_list = copy_family_expenses_list(family_expenses_list)
        list_of_versions_of_family_expenses_list.append(copy_of_family_expenses_list)
        if sign == "=":
            while index < len(family_expenses_list):
                current_expense = get_expense_from_list(family_expenses_list, index)
                current_category = get_expense_category(current_expense)
                current_amount_of_money = get_expense_amount_of_money(current_expense)
                if current_category != given_category or (current_category == given_category and
                                                          current_amount_of_money != given_amount_of_money):
                    family_expenses_list.pop(index)
                else:
                    index += 1
        elif sign == "<":
            while index < len(family_expenses_list):
                current_expense = get_expense_from_list(family_expenses_list, index)
                current_category = get_expense_category(current_expense)
                current_amount_of_money = get_expense_amount_of_money(current_expense)
                if current_category != given_category or (current_category == given_category and
                                                          current_amount_of_money >= given_amount_of_money):
                    family_expenses_list.pop(index)
                else:
                    index += 1
        else:
            while index < len(family_expenses_list):
                current_expense = get_expense_from_list(family_expenses_list, index)
                current_category = get_expense_category(current_expense)
                current_amount_of_money = get_expense_amount_of_money(current_expense)
                if current_category != given_category or (current_category == given_category and
                                                          current_amount_of_money <= given_amount_of_money):
                    family_expenses_list.pop(index)
                else:
                    index += 1
        if len(family_expenses_list) == 0:
            print("There were no expenses from " + given_category + " category, so all expenses were removed from list !")
        else:
            print("List was filtered successfully !")
        list_of_operations_that_modified_family_expenses_list.append("filter " + given_category + " " + sign + " " +
                                                                     str(given_amount_of_money))


def undo_operation(family_expenses_list, list_of_operations_that_modified_family_expenses_list,
                   list_of_versions_of_family_expenses_list):
    # This function undoes the last operation that modified the family expenses list.
    if len(list_of_operations_that_modified_family_expenses_list) == 0:
        print("There are no operations to undo !")
    else:
        family_expenses_list.clear()
        last_version_of_family_expenses_list = list_of_versions_of_family_expenses_list[len(list_of_versions_of_family_expenses_list) - 1]
        for expense in last_version_of_family_expenses_list:
            family_expenses_list.append(expense)
        print("The operation to undo is: " + list_of_operations_that_modified_family_expenses_list[len(list_of_versions_of_family_expenses_list) - 1])
        list_of_versions_of_family_expenses_list.pop()
        list_of_operations_that_modified_family_expenses_list.pop()
        print("The undo process was executed successfully !")
