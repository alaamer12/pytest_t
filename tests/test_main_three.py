from __future__ import annotations
import pytest
from main_three import *
import random


class TestMainThree:
    class TestAddTen:

        def test_add_ten(self):
            assert add_ten(5) == 15

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                add_ten("5")
            with pytest.raises(TypeError):
                add_ten([5.5])

    class TestReverseString:

        def test_reverse_string(self):
            assert reverse_string("hello") == "olleh"

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                reverse_string(5)

    class TestSumList:
        def test_sum_list(self):
            assert sum_list([1, 2, 3, 4, 5]) == 15
            assert sum_list([]) == 0
            assert sum_list([1, 2, 3, 4, 5, 60]) != 21

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                sum_list("5")
            with pytest.raises(TypeError):
                sum_list(5.5)

    class TestSortList:
        def test_sort_list(self):
            assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
            assert sort_list([1, 2, 3, 4, 60, 5]) != [1, 2, 3, 60, 4, 5]
            assert sort_list([]) == []

        def test_invalid_input(self):
            # Wont raise an error because string is iterable
            assert sort_list("5 2 4 8") != "8 5 4 2"
            with pytest.raises(TypeError):
                sort_list(5.5)

    class TestConvertDateFormat:
        def test_convert_date_format(self):
            assert convert_date_format("2024-04-10") == "10/04/2024"

        def test_invalid_input(self):
            with pytest.raises(ValueError):
                assert convert_date_format("2024-04-10 10:10:10") == "10/04/2024 10:10:10"
            with pytest.raises(TypeError):
                convert_date_format(5)
            with pytest.raises(ValueError):
                convert_date_format("%Y-%m-%d %H:%M:%S")
            with pytest.raises(ValueError):
                convert_date_format("10/04/2024 10:10:10")
            with pytest.raises(TypeError):
                convert_date_format(["10/04/2024", "10:10:10"])

    class TestSphereVolume:
        def test_sphere_volume(self):
            expected_volume = 523.6
            computed_volume = sphere_volume(5)
            assert round(computed_volume, 1) == expected_volume
            assert sphere_volume(5.5) != 523.6

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                sphere_volume("5")

            with pytest.raises(TypeError):
                sphere_volume([5.5])

    class TestRandomNumber:
        def test_random_number(self, monkeypatch):
            monkeypatch.setattr(random, 'randint', lambda x, y: 10)
            assert generate_random_number() == 10
            monkeypatch.setattr(random, 'randint', lambda x, y: 1)
            assert generate_random_number() != 10

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                generate_random_number("5")
            with pytest.raises(TypeError):
                generate_random_number([5.5])

    class TestRandomPassword:
        def test_random_password(self, monkeypatch):
            monkeypatch.setattr(random, 'choice', lambda x: 'a')
            assert generate_random_password(5) == 'aaaaa'
            assert generate_random_password(5) != 'aaaan'

        def test_invalid_input(self):
            with pytest.raises(TypeError):
                generate_random_password("5")
            with pytest.raises(TypeError):
                generate_random_password([5.5])
