# from unittest.mock import patch, MagicMock
# from main_five import FunctionCollection as MyClass
# import shutil
# import os
import pytest
#
# source = "main.py"
# destination = "main_copy.py"
#
# @pytest.mark.parametrize("input_values, expected_result", [
#     ([source, destination], f"File copied from '{source}' to '{destination}'.")
# ])
# def test_copy_file_success(input_values, expected_result, monkeypatch):
#     test_instance = MyClass()
#     monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
#     with patch('shutil.copy', MagicMock(return_value=None)) as mock_copy:
#         result = test_instance.copy_file()
#         mock_copy.assert_called_once_with(source, destination)
#         assert result == expected_result
def test_recursion_depth():
    with pytest.raises(ZeroDivisionError) as excinfo:
        X = 1 / 0
    with open("x.txt", "w") as w:
        w.write(str(excinfo))
        w.write(str(excinfo.type))
        w.write(str(excinfo.traceback))
        w.write(str(excinfo.value))
    assert "maximum recursion" not in str(excinfo.value)



class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket, ):
    assert my_fruit in fruit_basket