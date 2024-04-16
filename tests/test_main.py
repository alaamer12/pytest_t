from __future__ import annotations
import pytest
from main import greet, add, get_random_number, get_current_time, calculate_circle_area, calculate_fibonacci, \
    generate_permutations, is_email_valid
import random
import datetime
import math
import itertools


class TestMain:
    class TestGreet:
        def test_regular_name(self):
            assert greet("Alice") == "Hello, Alice!"

        def test_empty_name(self):
            assert greet("") == "Hello, !"

        def test_invalid_name(self):
            with pytest.raises(ValueError):
                greet(123)

    class TestAdd:
        def test_regular_numbers(self):
            assert add(3, 5) == 8

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                add(3, "5")

    class TestGetRandomNumber:

        # ! SEE
        def test_regular_numbers(self, monkeypatch):
            # Mocking random.randint to return 6
            monkeypatch.setattr(random, 'randint', lambda x, y: 6)
            assert get_random_number(1, 10) == 6

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                get_random_number(1, "10")

        def test_invalid_value_error(self):
            with pytest.raises(ValueError):
                get_random_number(1, 0)

    class TestCurrentTime:

        def test_current_time(self):
            assert get_current_time() == datetime.datetime.now().strftime("%H:%M:%S")

        def test_invalid_time(self):
            assert get_current_time() != "20:20:20"

    class TestCircleArea:

        def test_regular_numbers(self):
            assert calculate_circle_area(5) == math.pi * 5 ** 2

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                calculate_circle_area("5")

    class TestFibonacci:

        def test_regular_numbers(self):
            assert calculate_fibonacci(5) == 5

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                calculate_fibonacci("5")

    class TestGeneratePermutations:

        def test_regular_numbers(self):
            assert generate_permutations([1, 2, 3]) == list(itertools.permutations([1, 2, 3]))

        def test_regular_numbers_manually(self):
            assert generate_permutations([1, 2, 3]) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2),
                                                        (3, 2, 1)]

        def test_invalid_numbers(self):
            with pytest.raises(TypeError):
                generate_permutations(5)

    class TestValidEmail:

        def test_regular_email(self):
            assert is_email_valid("example@example.com") == True

        def test_invalid_email(self):
            assert not is_email_valid("example.com") == True

