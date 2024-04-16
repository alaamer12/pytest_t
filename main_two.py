from functools import reduce
import math

# Simple Functions
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def is_even(num: int) -> bool:
    """Check if a number is even."""
    return num % 2 == 0

# Intermediate Functions
def find_max(lst: list) -> float:
    """Find the maximum element in a list."""
    return max(lst)

def calculate_average(lst: list) -> float:
    """Calculate the average of numbers in a list."""
    return sum(lst) / len(lst)

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Advanced Functions
def calculate_factorial(n: int) -> int:
    """Calculate the factorial of a number."""
    return reduce(lambda x, y: x * y, range(1, n + 1))

def reverse_string(string: str) -> str:
    """Reverse a given string."""
    return string[::-1]

def count_vowels(string: str) -> int:
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return len([char for char in string if char in vowels])

# Super Advanced Functions
def generate_fibonacci_sequence(n: int) -> list:
    """Generate the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Testing the functions
if __name__ == "__main__":
    print(add_numbers(5, 3))  # Output: 8
    print(multiply_numbers(5, 3))  # Output: 15
    print(is_even(4))  # Output: True
    print(find_max([3, 7, 2, 9, 5]))  # Output: 9
    print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0
    print(is_prime(7))  # Output: True
    print(calculate_factorial(5))  # Output: 120
    print(reverse_string("hello"))  # Output: "olleh"
    print(count_vowels("hello"))  # Output: 2
    print(generate_fibonacci_sequence(8))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]
