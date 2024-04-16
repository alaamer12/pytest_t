import math
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import sqlite3
import shutil
import rsa
import sys



class FunctionCollection:
    def __init__(self):
        pass

    @staticmethod
    def get_random_joke():
        """Returns a random Chuck Norris joke."""
        response = requests.get("https://api.chucknorris.io/jokes/random")
        joke = response.json()["value"]
        return joke

    @staticmethod
    def get_cat_facts():
        """Returns the current weather of a city."""
        length = input("Enter length: ")
        url = f"https://catfact.ninja/fact?max_length={length}"
        response = requests.get(url)
        weather_data = response.json()
        return weather_data

    @staticmethod
    def list_files_in_directory():
        """Returns the names of all files in the current directory."""
        files = os.listdir()
        return files

    @staticmethod
    def get_wikipedia_page_title():
        """Returns the title of a Wikipedia page."""
        query = input("Enter search query: ")
        url = f"https://en.wikipedia.org/wiki/{query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title").text
        return title

    @staticmethod
    def create_new_directory():
        """Creates a new directory."""
        directory_name = input("Enter directory name: ")
        os.mkdir(directory_name)
        return f"Directory '{directory_name}' created."

    @staticmethod
    def get_file_size():
        """Returns the size of a file."""
        file_name = input("Enter file name: ")
        file_size = os.path.getsize(file_name)
        return f"Size of '{file_name}' is {file_size} bytes."

    @staticmethod
    def create_database_and_table():
        """Creates a SQLite database and table."""
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.commit()
        conn.close()
        return "Database and table created successfully."

    @staticmethod
    def copy_file():
        """Copies a file to a new location."""
        src = input("Enter source file path: ")
        dest = input("Enter destination file path: ")
        shutil.copy(src, dest)
        return f"File copied from '{src}' to '{dest}'."

    @staticmethod
    def generate_rsa_key_pair():
        """Generates an RSA key pair."""
        (public_key, private_key) = rsa.newkeys(512)
        return f"Public key: {public_key}\nPrivate key: {private_key}"

    @staticmethod
    def get_file_contents():
        """Returns the contents of a file using pathlib."""
        file_path = input("Enter file path: ")
        file_contents = Path(file_path).read_text()
        return file_contents


    @staticmethod
    def math_operated_on_numbers():
        """Returns the result of a mathematical operation on two numbers."""
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2
        else:
            return "Invalid operation"


# f = FunctionCollection()
# print(f.get_cat_facts())
# # Testing the methods
# print(FunctionCollection.get_random_joke())
# print(FunctionCollection.get_city_weather())
# print(FunctionCollection.list_files_in_directory())
# print(FunctionCollection.get_wikipedia_page_title())
# print(FunctionCollection.create_new_directory())
# print(FunctionCollection.get_file_size())
# print(FunctionCollection.create_database_and_table())
# print(FunctionCollection.copy_file())
# print(FunctionCollection.generate_rsa_key_pair())
# print(FunctionCollection.get_file_contents())
# print(FunctionCollection.calculate_square_root())
# print(FunctionCollection.list_installed_packages())






# Testing the methods
# print(UtilityFunctions.get_random_joke())
# print(UtilityFunctions.get_weather())
# print(UtilityFunctions.list_files_in_directory())
# print(UtilityFunctions.get_wikipedia_page_title())
# print(UtilityFunctions.create_directory())
# print(UtilityFunctions.get_file_size())
# print(UtilityFunctions.create_database_and_table())
# print(UtilityFunctions.copy_file())
# print(UtilityFunctions.generate_rsa_key_pair())
# print(UtilityFunctions.get_city_weather_description())