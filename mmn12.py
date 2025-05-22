"""
Name: Adi Pedel
Project: mmn12

Description:
This module contains several utility functions related to number theory, string compression,
and user interaction. The functions include prime checking, happy number detection, and
basic string manipulation.

Functions:
1. is_prime(n):
   Determines whether a given number n is a prime number.

2. max_prime():
   Continuously receives natural numbers from the user and returns the largest prime number entered.

3. compression(s):
   Compresses consecutive identical characters in a string into a single character followed by the count.

4. sum_square(num):
   Calculates the sum of the squares of the digits of a given number.

5. is_happy(num):
   Determines if a number is a "happy number" using the sum of squares of its digits.

6. count_happy_numbers():
   Counts how many numbers from 1 to 100 (inclusive) are happy numbers.

Usage:
Use this module to explore prime numbers, string compression techniques, and the concept of happy numbers.
Functions may be used individually or combined in larger projects related to number theory or user interaction.
"""


def is_prime(n):
    """
        Checks if a given number is prime.

        Parameters:
            n (int): The number to check.

        Returns:
            bool: True if n is a prime number, False otherwise.

        Notes:
            The function tests divisibility by all natural numbers from n-1 down to 2.
        """
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return False
    return True


def max_prime():
    """
        Continuously receives natural numbers from the user and finds the largest prime number entered.

        Returns:
            int: The largest prime number entered by the user.

        Notes:
            Input stops when the user enters a number less than 1.
        """
    num = max_prime_num = 1
    while num >= 1:
        num = int(input("Please enter a natural number: \n"))
        if is_prime(num) and num > max_prime_num:
            max_prime_num = num
    return max_prime_num


def compression(s):
    """
        Compresses a string by replacing consecutive repeated characters with the character followed by the count.

        Parameters:
            s (str): The input string to compress.

        Returns:
            str: The compressed string.

        Example:
            'aaadf' -> 'a3df'
        """
    i = 1
    num = 1
    while i < len(s):
        if  s[i] == s[i-1]:
            while i < len(s) and s[i] == s[i - 1]:
                num += 1
                i += 1
            s = s[0:i-num+1]+str(num)+s[i:]
            num = 1
            i-=1
        i+=1
    return s

def sum_square(num):
    """
        Calculates the sum of the squares of the digits of a number.

        Parameters:
            num (int): The input number.

        Returns:
            int: The sum of the squares of the digits of num.
        """
    num_sum = 0
    while num != 0:
        num_sum +=  (num % 10)*(num % 10)
        num = num // 10
    return num_sum


def is_happy(num):
    """
        Determines if a number is a happy number.

        Parameters:
            num (int): The number to check.

        Returns:
            bool: True if num is a happy number, False otherwise.

        Notes:
            A number is happy if repeatedly replacing it by the sum of the squares of its digits eventually equals 1.
            This function limits the check to 10 iterations to avoid infinite loops.
        """
    count = 0
    while count < 10:
        if num == 1:
            return True
        num = sum_square(num)
        count += 1
    return False


def count_happy_numbers():
    """
        Counts how many numbers between 1 and 100 (inclusive) are happy numbers.

        Returns:
            int: The count of happy numbers in the range 1 to 100.
        """
    count = 0
    for num in range(1, 101):
        if is_happy(num):
            count += 1
    return count