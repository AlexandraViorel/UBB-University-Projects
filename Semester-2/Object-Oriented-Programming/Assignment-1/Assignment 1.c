#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int* read_array(int* N) {
    // This function reads an array from user input with the size n, also given by the user.
    int n;
    printf_s("How many elements do you want to read?:");
    scanf_s("%d", &n);

    int* arr = (int*)malloc(sizeof(int) * n);
    if (NULL == arr)
    {
        return NULL;
    }
    for (int i = 0; i < n; i++)
    {
        scanf_s("%d", &arr[i]);
    }

    *N = n;
    return arr;
}

int is_prime(int x) {
    // This function verifies if the given number x is prime.
    // It returns 0 if the number isn't prime, and 1 otherwise
    int prim = (x > 1 && (x % 2 == 1 || x == 2));

    for (int d = 3; prim && d * d <= x; d += 2)
    {
        if (!(x % d))
        {
            return 0;
        }
    }

    return prim;
}

void write_the_first_n_prime_numbers() {
    // This function reads a number n and prints the first n prime numbers.
    int n;
    printf("how many prime numbers do you want to print? ");
    scanf_s("%d", &n);
    int i = 0;
    int x = 2;
    while (i < n) {
        if (is_prime(x) == 1) {
            printf("%d ", x);
            i++;
        }
        x += 1;
    }
}

int gcd(int a, int b) {
    // This function calculates the greatest common divisor of two given numbers a and b.
    int r;
    while (b) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

void longest_subsequence_of_relatively_prime_numbers(int v[], int n) {
    // This function prints the longest contiguous subsequence of relatively prime numbers from a 
    //given vector of size n.
    // Two numbers are relatively prime if their gcd is 1.
    int startcrt = 0, lcrt = 1, lmax = 1, start_max = 0;
    for (int i = 1; i < n; i++) {
        if (gcd(v[i], v[i - 1]) == 1) {
            lcrt++;
        }
        else {
            if (lcrt > lmax) {
                lmax = lcrt;
                start_max = startcrt;
            }
            startcrt = i;
            lcrt = 1;
        }
    }
    if (lcrt > lmax) {
        lmax = lcrt;
        start_max = startcrt;
    }
    int i = 0;
    while (i < lmax) {
        printf("%d ", v[start_max + i]);
        i++;
    }
}

int print_the_exponent() {
    // This function reads a number n and a prime number p, and prints the exponent of the number p from
    //the decomposition of n in prime factors.
    int n;
    printf("Write n: ");
    scanf_s("%d", &n);

    int p;
    printf("Write p (the base of the exponent you want to print): ");
    scanf_s("%d", &p);

    int f = 2;
    int exp = 0;
    while (n != 1) {
        while (n % f == 0 && n != 1) {
            n = n / f;
            exp++;
        }
        if (f == p) {
            printf("The exponent of the prime number p is: %d ", exp);
            return 0;
        }
        f++;
        exp = 0;
    }
    printf("The exponent of the prime number p is: 0");
}

void print_menu() {
    // This function prints the options menu.
    printf("\n --- OPTIONS MENU --- \n");
    printf("1. Read a vector \n");
    printf("2. Generate the first n prime numbers \n");
    printf("3. Find the longest subsequence such that any two consecutive elements are relatively prime \n");
    printf("4. Print the exponent of a prime number p from the decomposition in prime factors of n \n");
    printf("5. Exit \n");
    printf("Choose your option: ");
}

int main() {
    // This is the main function.
    int n;
    int option;
    int* array = NULL;
    while (1) {
        print_menu();
        scanf_s("%d", &option);
        if (option == 1) {
            array = read_array(&n);
            if (NULL == array)
            {
                printf("reading failed!");
                return 0;
            }
        }
        else if (option == 2) {
            write_the_first_n_prime_numbers();
        }
        else if (option == 3) {
            if (NULL == array)
            {
                printf("you haven't read a vector !! ");
            }
            else {
                longest_subsequence_of_relatively_prime_numbers(array, n);
            }
        }
        else if (option == 4) {
            print_the_exponent();
        }
        else if (option == 5) {
            printf("you exit the program !");
            return 0;
        }
        else {
            printf("Invalid option ! Try another one! ");
        }
    }
    return 0;
}