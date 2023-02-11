# Solve the problem from the first set here
# 4. For a given natural number n find the largest natural number written with the same digits. (e.g. n=3658, m=8653).

def create_list(digits, n):
    """
    :param digits: here we put all the digits of the number n
    :param n: the given number
    This function creates a list named digits using all the digits of the number n.
    """
    while n > 0:
        c = int(n % 10)
        digits.append(c)
        n = int(n / 10)

def sort_list(digits):
    # This function sorts the list "digits" in descending order.
    for i in range(len(digits)-1):
        for j in range(i,len(digits)):
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]

def find_largest_number(digits):
    # This function writes the largest number m using the digits from the list "digits".
    m = int(0)
    for i in range(len(digits)):
        m = m * 10 + int(digits[i])
    print("The largest number is :" + str(m))

def solve():
    # This is the "main" function, where we use all the functions created above in order to solve the problem.
    digits = []
    n = int(input("Write n="))
    create_list(digits, n)
    sort_list(digits)
    find_largest_number(digits)


solve()