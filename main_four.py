import random
from typing import List
import math


class FunctionCollection:
    def __init__(self, value: int):
        self.value = value

    # def __new__(


    @staticmethod
    def sum_numbers():
        """Returns a function that calculates the sum of two numbers."""
        return lambda x, y: x + y

    @staticmethod
    def square_root():
        """Returns a function that calculates the square root of a number."""
        return lambda x: math.sqrt(x)

    @staticmethod
    def primes_up_to_limit():
        """Returns a function that calculates the list of prime numbers up to a given limit."""

        def calculate_primes_up_to(limit: int) -> List[int]:
            def is_prime(num: int) -> bool:
                if num < 2:
                    return False
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        return False
                return True

            return [num for num in range(2, limit + 1) if is_prime(num)]

        return calculate_primes_up_to

    @staticmethod
    def sum_of_digits():
        """Returns a function that calculates the sum of digits of a given number."""

        def calculate_sum_of_digits(num: int) -> int:
            return sum(int(digit) for digit in str(num))

        return calculate_sum_of_digits

    @staticmethod
    def triangular_number():
        """Returns a function that calculates the nth triangular number."""

        def calculate_triangular_number(n: int) -> int:
            return n * (n + 1) // 2

        return calculate_triangular_number

    @staticmethod
    def calculate_square():
        """Returns the square of a given number."""
        num = float(input("Enter a number: "))
        return num ** 2

    @staticmethod
    def calculate_hypotenuse():
        """Returns the hypotenuse of a right triangle given its two sides."""
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        return math.sqrt(side1 ** 2 + side2 ** 2)

    @staticmethod
    def generate_primes():
        """Returns a list of prime numbers up to a given limit."""
        limit = int(input("Enter a limit: "))
        primes = []
        for num in range(2, limit + 1):
            if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
                primes.append(num)
        return primes

    @staticmethod
    def check_palindrome():
        """Checks if a given string is a palindrome."""
        string = input("Enter a string: ")
        return string == string[::-1]

    @classmethod
    def calculate_median(cls):
        """Returns the median of a list of numbers."""
        num_list = input("Enter numbers separated by space: ").split()
        num_list = [float(x) for x in num_list]
        num_list.sort()
        length = len(num_list)
        if length % 2 == 0:
            return (num_list[length // 2 - 1] + num_list[length // 2]) / 2
        else:
            return num_list[length // 2]


# Testing the methods
func_col = FunctionCollection(10)


# Testing the methods
# print(func_col.calculate_square())
# print(func_col.calculate_hypotenuse())
# print(func_col.generate_primes())
# print(func_col.check_palindrome())
# print(func_col.calculate_median())
#
#
# print(func_col.sum_numbers()(3, 7))  # Output: 10
# print(func_col.square_root()(9))  # Output: 3.0
# print(func_col.primes_up_to_limit()(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
# print(func_col.sum_of_digits()(12345))  # Output: 15
# print(func_col.triangular_number()(5))  # Output: 15
