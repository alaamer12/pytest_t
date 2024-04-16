from __future__ import annotations
import pytest
from main_two import *


class TestMainTwo:
    class TestAddNumbers:

        def test_regular_numbers(self):
            assert add_numbers(3, 5) == 8

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                add_numbers(3, "5")

    class TestMutlipyNumbers:

        def test_regular_numbers(self):
            assert multiply_numbers(3, 5) == 15

        def test_invalid_numbers(self):
            assert not isinstance(multiply_numbers(3, "5"), int)

    class TestIsEven:
        def test_regular_numbers(self):
            assert is_even(4) == True

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                is_even("5")

        def test_invalid_even(self):
            assert is_even(3) == False

    class TestFindMax:
        def test_regular_numbers(self):
            assert find_max([10, 20, 30]) == 30

        def test_invalid_numbers(self):
            # It returns 3 based on comparison of 10, 20, 30 as ASCII
            assert find_max("10, 20, 30") != 30

        def test_invalid_Value_error(self):
            assert find_max(['10', '20', '0']) != 30

    class TestIsPrime:
        def test_regular_numbers(self):
            assert is_prime(5) == True

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                is_prime("5")

    class TestCalculateAverage:
        def test_regular_numbers(self):
            assert calculate_average([10, 20, 30]) == 20

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                calculate_average("10, 20, 30")

    class TestCalculateFactorial:
        def test_regular_numbers(self):
            assert calculate_factorial(5) == 120

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                calculate_factorial("5")

        def test_invalid_Value_error(self):
            with pytest.raises(TypeError):
                calculate_factorial(-10)

    class TestReverseString:
        def test_regular_numbers(self):
            assert reverse_string("hello") == "olleh"

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                reverse_string(5)

    class TestCountVowels:
        def test_regular_numbers(self):
            assert count_vowels("hello") == 2

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                count_vowels(5)

        def test_invalid_Value(self):
            assert count_vowels("hello") != 3

    class TestGenerateFibonacciSequence:
        def test_regular_numbers(self):
            assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                generate_fibonacci_sequence("5")

        def test_invalid_value(self):
            assert generate_fibonacci_sequence(-10) == []

