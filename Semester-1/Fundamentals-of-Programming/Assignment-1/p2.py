# Solve the problem from the second set here
"""
6.Determine a calendar date (as year, month, day) starting from two integer numbers representing the year and the
day number inside that year (e.g. day number 32 is February 1st).
Take into account leap years. Do not use Python's inbuilt date/time functions.
"""

def is_leap_year(year):
    # This function verifies if the year given is a leap year or not.
    lyear = 2020
    while year < lyear:
        year = year + 4
    if year == lyear:
        return True
    else:
        return False

def create_list(year):
    # This function creates a list with the number of days each month contains.
    months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        months[2] = 29
    return months

def determine_day_and_month(year, x, months):
    # This function determines the day and the month.
    i = int(0)
    n = int(0)
    while i <= 12 and n < x:
        i = i + 1
        n = n + int(months[i])
    j = int(i)
    while n > x and j > 1:
        n = n - months[j]
        j = j - 1
    if n == x:
        day = x
    else:
        day = x - n
    month = i
    print("The calendar date is: " + str(year) + "/" + str(month) + "/" + str(day))

def solve():
    # This is the "main" function, where we use all the functions created above in order to solve the problem.
    year = int(input("Write the year"))
    x = int(input("Write the number"))
    months = create_list(year)
    determine_day_and_month(year, x, months)

solve()