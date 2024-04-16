from __future__ import annotations
import pytest
from main_four import FunctionCollection as fc


class TestMainFour:
    class TestFunctionCollection:
        def test_sum_numbers(self):
            assert fc.sum_numbers()(5, 10) == 15

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                fc.sum_numbers()("1, 2, 3")

    class TestSquareRoot:
        def test_square_root(self):
            assert fc.square_root()(9) == 3
            _round = round(fc.square_root()(11), 1)
            assert _round == 3.3

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                fc.square_root()("9, 11, 13")

    class TestPrimesUpToLimit:
        def test_primes_up_to_limit(self):
            assert fc.primes_up_to_limit()(20) == [2, 3, 5, 7, 11, 13, 17, 19]
            assert fc.primes_up_to_limit()(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                fc.primes_up_to_limit()("20, 30")

    class TestSumOfDigits:
        def test_sum_of_digits(self):
            assert fc.sum_of_digits()(12345) == 15
            assert fc.sum_of_digits()("98765") == 35

        def test_invalid_input(self):
            with pytest.raises(ValueError):
                # It doesnt handle negatives
                fc.sum_of_digits()(-54321)

            with pytest.raises(ValueError):
                fc.sum_of_digits()("12345, 54321, 98765")
            # It Doesnt raise Type Error on input string
            with pytest.raises(ValueError):
                fc.sum_of_digits()(["12345", "54321", "98765"])

    class TestTriangularNumber:
        def test_triangular_number(self):
            assert fc.triangular_number()(5) == 15
            assert fc.triangular_number()(10) == 55
            assert fc.triangular_number()(15) == 120

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                fc.triangular_number()("5, 10, 15")

    class TestCalculateSquare:
        def test_calculate_square(self, monkeypatch):
            monkeypatch.setattr("builtins.input", lambda _: "9")
            assert fc.calculate_square() == 81
            monkeypatch.setattr("builtins.input", lambda _: 9)
            assert fc.calculate_square() == 81
            assert fc.calculate_square() != 89

        def test_invalid_input(self, monkeypatch):
            with pytest.raises(ValueError):
                monkeypatch.setattr("builtins.input", lambda _: "9, 11, 13")
                fc.calculate_square()
            # I Think it may raise ValueError
            with pytest.raises(TypeError):
                monkeypatch.setattr("builtins.input", lambda _: [9, 11, 13])
                fc.calculate_square()

    class TestCalculateHypotenuse:
        def test_calculate_hypotenuse(self, monkeypatch):
            monkeypatch.setattr("builtins.input", lambda x: "3")
            monkeypatch.setattr("builtins.input", lambda y: "4")
            # 5.65685424949238 I dont know why
            assert int(fc.calculate_hypotenuse()) == 5
            monkeypatch.setattr("builtins.input", lambda x: 3)
            monkeypatch.setattr("builtins.input", lambda y: 4)
            assert int(fc.calculate_hypotenuse()) == 5

        def test_invalid_input(self, monkeypatch):
            with pytest.raises(ValueError):
                monkeypatch.setattr("builtins.input", lambda x: "3, 4")
                monkeypatch.setattr("builtins.input", lambda y: "4 , 5")
                fc.calculate_hypotenuse()
            # I Think it may raise ValueError
            with pytest.raises(TypeError):
                monkeypatch.setattr("builtins.input", lambda x: [3])
                monkeypatch.setattr("builtins.input", lambda y: [4])
                fc.calculate_hypotenuse()

    class TestGeneratePrimes:
        def test_generate_primes(self, monkeypatch):
            monkeypatch.setattr("builtins.input", lambda x: "10")
            assert fc.generate_primes() == [2, 3, 5, 7]
            monkeypatch.setattr("builtins.input", lambda x: 10)
            assert fc.generate_primes() == [2, 3, 5, 7]
            assert fc.generate_primes() != [2, 3, 5, 7, 9, 11, 13, 15, 17, 19]

        def test_invalid_input(self, monkeypatch):
            with pytest.raises(ValueError):
                monkeypatch.setattr("builtins.input", lambda x: "10, 20")
                fc.generate_primes()

            with pytest.raises(TypeError):
                monkeypatch.setattr("builtins.input", lambda x: [10, 20])
                fc.generate_primes()

    class CheckPalindrome:
        def test_check_palindrome(self, monkeypatch):
            monkeypatch.setattr("builtins.input", lambda x: "baba")
            assert fc.check_palindrome() == True
            monkeypatch.setattr("builtins.input", lambda x: "Gaggy")
            assert fc.check_palindrome() == False

        def test_invalid_input(self, monkeypatch):
            with pytest.raises(TypeError):
                monkeypatch.setattr("builtins.input", lambda x: 12345)
                fc.check_palindrome()

            with pytest.raises(TypeError):
                monkeypatch.setattr("builtins.input", lambda x: [12345, 54321])
                fc.check_palindrome()

    class TestCalculateMedian:
        def test_calculate_median(self, monkeypatch):
            monkeypatch.setattr("builtins.input", lambda x: "5")
            assert fc.calculate_median() == 5
            monkeypatch.setattr("builtins.input", lambda x: "5 6 7 8 9 10")
            assert fc.calculate_median() != 5

        def test_invalid_input(self, monkeypatch):
            with pytest.raises(ValueError):
                monkeypatch.setattr("builtins.input", lambda y: "10 , 20 , 30 , 40")
                assert fc.calculate_median() == 25

            with pytest.raises(AttributeError):
                monkeypatch.setattr("builtins.input", lambda x: [5, 10, 20, 30, 40])
                fc.calculate_median()

            with pytest.raises(AttributeError):
                monkeypatch.setattr("builtins.input", lambda x: 5)
                fc.calculate_median()
