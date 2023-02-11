"""
  Start the program by running this module
"""


from ui import *
from functions import *


def start_command():
    run_all_tests()
    family_expenses_list = initialize_family_expenses_list()
    list_of_versions_of_family_expenses_list = create_list_of_versions_of_family_expenses_list()
    list_of_operations_that_modified_family_expenses_list = create_list_of_operations_that_modified_family_expenses_list()

    while True:
        command = input("prompt> ")
        command_word1, command_word2, command_parameters = split_command(command)

        try:
            if command_word1 == "add" and command_word2 is None:
                add_expenses_to_current_day(family_expenses_list, command_parameters,
                                            list_of_operations_that_modified_family_expenses_list,
                                            list_of_versions_of_family_expenses_list)
            elif command_word1 == "insert" and command_word2 is None:
                insert_expenses_to_chosen_day(family_expenses_list, command_parameters,
                                              list_of_operations_that_modified_family_expenses_list,
                                              list_of_versions_of_family_expenses_list)
            elif command_word1 == "remove" and command_word2 is None:
                if verify_one_command_parameter(command_parameters) == "a day":
                    remove_expenses_from_specified_day(family_expenses_list, command_parameters,
                                                       list_of_operations_that_modified_family_expenses_list,
                                                       list_of_versions_of_family_expenses_list)
                elif verify_one_command_parameter(command_parameters) == "a category":
                    remove_expenses_from_specified_category(family_expenses_list, command_parameters,
                                                            list_of_operations_that_modified_family_expenses_list,
                                                            list_of_versions_of_family_expenses_list)
                else:
                    print("Invalid parameters !")
            elif command_word1 == "remove" and command_word2 == "to":
                remove_expenses_from_day1_to_day2(family_expenses_list, command_parameters,
                                                  list_of_operations_that_modified_family_expenses_list,
                                                  list_of_versions_of_family_expenses_list)
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
            elif command_word1 == "sum" and command_word2 is None:
                display_category_sum(family_expenses_list, command_parameters)
            elif command_word1 == "max" and command_word2 == "day":
                display_the_day_with_maximum_expenses(family_expenses_list, command_parameters)
            elif command_word1 == "sort" and command_word2 == "day":
                display_total_daily_expenses_in_ascending_order_by_amount_of_money_spent(family_expenses_list,
                                                                                         command_parameters)
            elif command_word1 == "sort" and command_word2 is None:
                display_expenses_for_given_category_in_ascending_order_by_amount_of_money_spent(family_expenses_list,
                                                                                                command_parameters)
            elif command_word1 == "filter" and command_word2 is None:
                filter_by_given_category(family_expenses_list, command_parameters,
                                         list_of_operations_that_modified_family_expenses_list,
                                         list_of_versions_of_family_expenses_list)
            elif command_word1 == "filter" and command_word2 in ["<", "=", ">"]:
                filter_by_given_category_and_given_amount_of_money_range(family_expenses_list, command_parameters,
                                                                         command_word2, list_of_operations_that_modified_family_expenses_list,
                                                                         list_of_versions_of_family_expenses_list)
            elif command_word1 == "undo" and command_word2 is None and command_parameters is None:
                undo_operation(family_expenses_list, list_of_operations_that_modified_family_expenses_list,
                               list_of_versions_of_family_expenses_list)
            elif command_word1 == "exit" and command_word2 is None and command_parameters is None:
                return
            else:
                print("Command does not exist !")
        except ValueError as value_error_var:
            print(str(value_error_var))


start_command()
