#
# Write the implementation for A2 in this file
#

import math

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities


def print_complex_number_with_positive_imaginary_part(complex_number, count):
    # This function prints a complex number that has the imaginary part positive.
    real_part = get_real_part(complex_number)
    imaginary_part = get_imaginary_part(complex_number)
    if real_part == 0:
        print(str(count) + ": " + str(imaginary_part) + "i")
    elif imaginary_part == 0:
        print(str(count) + ": " + str(real_part))
    else:
        print(str(count) + ": " + str(real_part) + "+" + str(imaginary_part) + "i")


def print_complex_number_with_negative_imaginary_part(complex_number, count):
    # This function prints a complex number that has the imaginary part negative.
    real_part = get_real_part(complex_number)
    imaginary_part = get_imaginary_part(complex_number)
    if real_part == 0:
        print(str(count) + ": " + str(imaginary_part) + "i")
    elif imaginary_part == 0:
        print(str(count) + ": " + str(real_part))
    else:
        print(str(count) + ": " + str(real_part) + str(imaginary_part) + "i")


def add_complex_number_to_list(complex_numbers_list):
    # This function adds a complex number to the complex numbers list.
    real_part = float(input("Enter the real part: "))
    imaginary_part = float(input("Enter the imaginary part: "))
    complex_number = create_complex_number(real_part, imaginary_part)
    complex_numbers_list.append(complex_number)
    print("Complex number added successfully !")


def show_the_entire_list_of_complex_numbers(complex_numbers_list):
    # This function shows all the complex numbers from the list.
    count = 1
    for complex_number in complex_numbers_list:
        imaginary_part = get_imaginary_part(complex_number)
        if imaginary_part < 0:
            print_complex_number_with_negative_imaginary_part(complex_number, count)
        else:
            print_complex_number_with_positive_imaginary_part(complex_number, count)
        count += 1


def print_longest_sequence_of_complex_numbers_with_modulus_in_range_0_10(complex_numbers_list):
    #  This function prints the longest sequence from the complex numbers list with the property that
    # all the numbers in the sequence have the modulus in range [0,10]. (property 8)
    maximum_length_of_sequence, first_position_of_the_longest_sequence, last_position_of_the_longest_sequence = \
        determine_longest_sequence_of_complex_numbers_with_modulus_in_range_0_10(complex_numbers_list)
    count = first_position_of_the_longest_sequence
    print("The longest sequence with the property that the modulus of all elements is in the [0, 10] range has " +
          str(maximum_length_of_sequence) + " elements, and the numbers are: ")
    for i in range(first_position_of_the_longest_sequence, last_position_of_the_longest_sequence):
        if complex_numbers_list[i][1] >= 0:
            print_complex_number_with_positive_imaginary_part(complex_numbers_list[i], count)
        else:
            print_complex_number_with_negative_imaginary_part(complex_numbers_list[i], count)
        count += 1


def print_longest_sequence_of_consecutive_complex_numbers_with_equal_sum(complex_numbers_list):
    #  This function prints the longest sequence from the complex numbers list with the property that all
    # the consecutive number pairs from the sequence have the same sum. (property 9)
    maximum_length_of_sequence, first_position_of_the_longest_sequence, last_position_of_the_longest_sequence = \
        determine_longest_sequence_of_pairs_of_consecutive_complex_numbers_with_equal_sum(complex_numbers_list)
    count = first_position_of_the_longest_sequence
    print("The longest sequence with the property that consecutive number pairs have equal sum has " +
          str(maximum_length_of_sequence) + " elements, and the numbers are: ")
    for i in range(first_position_of_the_longest_sequence, last_position_of_the_longest_sequence):
        if complex_numbers_list[i][1] >= 0:
            print_complex_number_with_positive_imaginary_part(complex_numbers_list[i], count)
        else:
            print_complex_number_with_negative_imaginary_part(complex_numbers_list[i], count)
        count += 1


def print_menu():
    # This function prints the menu.
    print("1. Add complex number")
    print("2. Show all complex numbers")
    print("3. Print the longest sequence with the property that the modulus of all elements is in the [0, 10] range")
    print("4. Print the longest sequence with the property that consecutive number pairs have equal sum")
    print("5. Exit")


def start_program():
    complex_numbers_list = initialize_the_list_of_complex_numbers()
    while True:
        print_menu()
        option = int(input("Enter your option: "))
        if option == 1:
            add_complex_number_to_list(complex_numbers_list)
        elif option == 2:
            show_the_entire_list_of_complex_numbers(complex_numbers_list)
        elif option == 3:
            print_longest_sequence_of_complex_numbers_with_modulus_in_range_0_10(complex_numbers_list)
        elif option == 4:
            print_longest_sequence_of_consecutive_complex_numbers_with_equal_sum(complex_numbers_list)
        elif option == 5:
            return
        else:
            print("This option does not exist !")


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

# print('Hello A2'!) -> prints aren't allowed here!

def create_complex_number(real_part, imaginary_part):
    return [real_part, imaginary_part]


def initialize_the_list_of_complex_numbers():
    """
    This function creates a list with 10 complex numbers.
    :return: the list of complex numbers
    """
    return [create_complex_number(1, 1), create_complex_number(1, 5), create_complex_number(1, 1),
            create_complex_number(1, 5), create_complex_number(0, -2), create_complex_number(13, 3),
            create_complex_number(4, 0), create_complex_number(1, -2), create_complex_number(5, 5),
            create_complex_number(3, 2)]


def get_real_part(complex_number):
    return complex_number[0]


def get_imaginary_part(complex_number):
    return complex_number[1]


def calculate_modulus_of_complex_number(complex_number):
    """
    This function calculates the modulus of a complex number
    :param complex_number: the list that contains the real and the imaginary parts of a complex number
    :return: the modulus of the given complex number
    """
    real_part = get_real_part(complex_number)
    imaginary_part = get_imaginary_part(complex_number)
    modulus = math.sqrt(real_part * real_part + imaginary_part * imaginary_part)
    return modulus


def determine_longest_sequence_of_complex_numbers_with_modulus_in_range_0_10(complex_numbers_list):
    """
    This function determines the maximum length and the positions of the first and last elements of the longest sequence
    with the property that every number in this sequence has the modulus in range [0,10].
    :param complex_numbers_list: the list that contains all the complex numbers
    :return: the maximum length and the positions of the first and last elements from the sequence of maximum length
    """
    maximum_length_of_sequence = 0
    position_of_the_first_element_of_the_longest_sequence = 0
    position_of_the_last_element_of_the_longest_sequence = 0
    i = 0
    while i <= len(complex_numbers_list) - 1:
        current_length_of_sequence = 0
        position_of_the_first_element_of_the_current_sequence = i
        position_of_the_last_element_of_the_current_sequence = i
        modulus = calculate_modulus_of_complex_number(complex_numbers_list[i])
        while 0 <= modulus <= 10 and i <= len(complex_numbers_list) - 1:
            current_length_of_sequence += 1
            position_of_the_last_element_of_the_current_sequence += 1
            i += 1
            if i < len(complex_numbers_list):
                modulus = calculate_modulus_of_complex_number(complex_numbers_list[i])
        if current_length_of_sequence > maximum_length_of_sequence:
            maximum_length_of_sequence = current_length_of_sequence
            position_of_the_first_element_of_the_longest_sequence = position_of_the_first_element_of_the_current_sequence
            position_of_the_last_element_of_the_longest_sequence = position_of_the_last_element_of_the_current_sequence
        i += 1
    return maximum_length_of_sequence, position_of_the_first_element_of_the_longest_sequence, \
           position_of_the_last_element_of_the_longest_sequence


def are_sums_equal(sum1, sum2):
    return sum1 == sum2


def calculate_sum_of_two_complex_numbers(complex_number1, complex_number2):
    """
    This function calculates the sum of two complex numbers.
    :param complex_number1: the first complex number
    :param complex_number2: the second complex number
    :return: the real and the imaginary part of the complex number obtained by summing two complex numbers
    """
    real_part_sum = get_real_part(complex_number1) + get_real_part(complex_number2)
    imaginary_part_sum = get_imaginary_part(complex_number1) + get_imaginary_part(complex_number2)
    return real_part_sum, imaginary_part_sum


def determine_longest_sequence_of_pairs_of_consecutive_complex_numbers_with_equal_sum(complex_numbers_list):
    """
    This function determines the maximum length and the positions of the first and last elements of the longest sequence
    with the property that every pair of two consecutive numbers in this sequence has the same sum.
    :param complex_numbers_list: the list that contains all the complex numbers
    :return: the maximum length and the positions of the first and last elements from the sequence of maximum length
    """
    maximum_length_of_sequence = 0
    position_of_the_first_element_of_the_longest_sequence = 0
    position_of_the_last_element_of_the_longest_sequence = 0
    i = 1
    while i < len(complex_numbers_list) - 1:
        current_length_of_sequence = 2
        position_of_the_first_element_of_the_current_sequence = i - 1
        position_of_the_last_element_of_the_current_sequence = i + 1
        sum1 = calculate_sum_of_two_complex_numbers(complex_numbers_list[i - 1], complex_numbers_list[i])
        sum2 = calculate_sum_of_two_complex_numbers(complex_numbers_list[i], complex_numbers_list[i + 1])
        while sum1 == sum2 and i < len(complex_numbers_list) - 1:
            current_length_of_sequence += 1
            position_of_the_last_element_of_the_current_sequence += 1
            i += 1
            if i < len(complex_numbers_list) - 1:
                sum1 = calculate_sum_of_two_complex_numbers(complex_numbers_list[i - 1], complex_numbers_list[i])
                sum2 = calculate_sum_of_two_complex_numbers(complex_numbers_list[i], complex_numbers_list[i + 1])
        if current_length_of_sequence > maximum_length_of_sequence:
            maximum_length_of_sequence = current_length_of_sequence
            position_of_the_first_element_of_the_longest_sequence = position_of_the_first_element_of_the_current_sequence
            position_of_the_last_element_of_the_longest_sequence = position_of_the_last_element_of_the_current_sequence
        i += 1
    return maximum_length_of_sequence, position_of_the_first_element_of_the_longest_sequence, \
           position_of_the_last_element_of_the_longest_sequence


start_program()
