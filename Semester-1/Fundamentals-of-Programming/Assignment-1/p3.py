# Solve the problem from the third set here
"""
15. Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message
should be displayed.
A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).
"""

def perfect_number(x):
    # This function verifies if the number "x" is a perfect number.
    sum = 0
    for divisor in range(1, int(x/2) + 1):
        if x % divisor == 0:
            sum = sum + divisor
    return sum == x

def generate_largest_perfect_number(n):
    # This function generates the largest perfect number smaller than the given number "n" or a message if such a number
    # doesn't exist.
    x = n - 1
    while x > 1 and perfect_number(x) == False:
        x = x - 1
    if x == 0 or x == 1:
        return "A perfect number smaller than " + str(n) + " doesn't exist !"
    else:
        return "The largest perfect number smaller than " + str(n) + " is " + str(x)

def solve():
    # This is the "main" function, where we use all the functions created above in order to solve the problem.
    n = int(input("Write n: "))
    print(generate_largest_perfect_number(n))

solve()