import math
import random
from datetime import datetime, timedelta
from typing import Optional

# Simple Functions
def add_ten(x: int) -> int:
    """Adds 10 to the input."""
    return x + 10

def reverse_string(s: str) -> str:
    """Reverses a string."""
    return s[::-1]

# Intermediate Functions
def sum_list(lst: list) -> int:
    """Calculates the sum of a list of numbers."""
    return sum(lst)

def sort_list(lst: list) -> list:
    """Sorts a list of numbers."""
    return sorted(lst)

# Advanced Functions
def convert_date_format(date_str: str) -> str:
    """Converts a date string to a different format."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%d/%m/%Y')

def sphere_volume(radius: float) -> float:
    """Calculates the volume of a sphere given its radius."""
    return (4 / 3) * math.pi * (radius ** 3)

# Super Advanced Functions
def generate_random_number() -> int:
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

def generate_random_password(n: int) -> str:
    """Generates a random password."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''.join(random.choice(characters) for _ in range(n))
    return password

# Sample usage
print(add_ten(5))  # Output: 15
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
print(convert_date_format("2024-04-10"))  # Output: "10/04/2024"
print(generate_random_number())  # Output: Random number between 1 and 100
