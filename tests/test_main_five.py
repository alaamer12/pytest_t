import pytest
import requests_mock
from main_five import FunctionCollection as fnc
import os
import sqlite3
import rsa
from pathlib import Path
from unittest.mock import patch, MagicMock
import shutil

FACT = ("The average lifespan of an outdoor-only cat is about 3 to 5 years while an indoor-only cat can live 16 years "
        "or much longer.")


source = "main.py"

destination = "main_copy.py"


class TestMainFive:
    @pytest.fixture
    def mock_response(self):
        with requests_mock.Mocker() as m:
            m.get('https://api.chucknorris.io/jokes/random', json={"value": "Chuck Norris can divide by zero."})
            m.get('https://catfact.ninja/fact?max_length=255', json={"fact": FACT})
            yield m

    def test_get_random_joke(self, mock_response):
        joke = fnc.get_random_joke()
        assert joke == "Chuck Norris can divide by zero."

    def test_get_cat_facts(self, mock_response, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda length: 255)
        fact = fnc.get_cat_facts()
        assert fact["fact"] == FACT

    def test_create_new_directory(self, monkeypatch):
        directory_name = "test_directory"
        if os.path.exists(directory_name):
            os.removedirs(directory_name)
        monkeypatch.setattr("builtins.input", lambda _: directory_name)
        result = fnc.create_new_directory()
        assert os.path.exists(directory_name)
        assert result == f"Directory '{directory_name}' created."
        os.removedirs(directory_name)

    def test_get_file_size(self, monkeypatch):
        file = "main.py"
        monkeypatch.setattr("builtins.input", lambda _: file)
        result = fnc.get_file_size()
        assert result == f"Size of '{file}' is {os.path.getsize(file)} bytes."

    @staticmethod
    @pytest.fixture
    def in_memory_db():
        # Create an in-memory SQLite database
        conn = sqlite3.connect(":memory:")
        yield conn
        conn.close()

    @staticmethod
    @pytest.fixture
    def test_database():
        # Create an in-memory SQLite database
        conn = sqlite3.connect("test.db")
        yield conn
        conn.close()

    def test_create_database_and_table(self, in_memory_db):
        result = fnc.create_database_and_table()
        cursor = in_memory_db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        assert cursor.fetchone() is None
        assert result == "Database and table created successfully."

    def test_create_database_and_table_two(self, in_memory_db):
        fnc.create_database_and_table()
        cursor = in_memory_db.cursor()
        # Create a new table
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        # Add data to the new table
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
        # Query the new table
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        assert len(results) == 1
        assert results[0] == (1, 'Alice', 25)

    def test_create_database_and_table_with_db(self, test_database):
        result = fnc.create_database_and_table()
        cursor = test_database.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        assert cursor.fetchone() is not None
        assert result == "Database and table created successfully."

    def test_create_database_and_table_two_with_db(self, test_database):
        fnc.create_database_and_table()
        cursor = test_database.cursor()
        # Create a new table
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        # Add data to the new table
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
        # Query the new table
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        assert len(results) == 1
        assert results[0] == (1, 'Alice', 25)

    @pytest.mark.parametrize("input_values, expected_result", [
        ([source, destination], f"File copied from '{source}' to '{destination}'.")
    ])
    def test_copy(self, input_values, expected_result, monkeypatch):
        test_instance = fnc()
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        # with patch('shutil.copy', MagicMock(return_value=None)) as mock_copy:
        #     result = test_instance.copy_file()
        #     mock_copy.assert_called_once_with(source, destination)
        #     assert result == expected_result
        monkeypatch.setattr(shutil, "copy", lambda x, y: None)
        assert test_instance.copy_file() == expected_result

    def test_generate_rsa_key_pair(self, monkeypatch):
        monkeypatch.setattr(rsa, "newkeys", lambda x: ("public_key", "private_key"))
        result = fnc.generate_rsa_key_pair()
        assert result == "Public key: public_key\nPrivate key: private_key"

    def test_get_file_contents(self, monkeypatch):
        file = "main.py"
        monkeypatch.setattr("builtins.input", lambda _: file)
        result = fnc.get_file_contents()
        assert result == Path(file).read_text()
        assert result == open(file).read()


    class TestMath:
        def test_addition_positive_numbers(self, monkeypatch):
            inputs = iter(["5", "3", "+"])
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            assert fnc.math_operated_on_numbers() == 8

        def test_subtraction_negative_numbers(self, monkeypatch):
            inputs = iter(["-5", "3", "-"])
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            assert fnc.math_operated_on_numbers() == -8

        def test_multiplication_with_zero(self, monkeypatch):
            inputs = iter(["5", "0", "*"])
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            assert fnc.math_operated_on_numbers() == 0

        def test_division_non_zero_numbers(self, monkeypatch):
            inputs = iter(["10", "2", "/"])
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            assert fnc.math_operated_on_numbers() == 5

        def test_invalid_operation(self, monkeypatch):
            inputs = iter(["1", "2", "%"])
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            assert fnc.math_operated_on_numbers() == "Invalid operation"

