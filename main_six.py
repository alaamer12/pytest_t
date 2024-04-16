import os
from pathlib import Path

class FileOperations:
    path = ""

    @classmethod
    def get_path(cls, file_name):
        """Get the path of the file."""
        cls.path = Path(file_name)
        return cls.path

    @classmethod
    def parse_path(cls):
        """Parse the path and return the directory and file name."""
        directory = cls.path.parent
        file_name = cls.path.name
        return directory, file_name

    @classmethod
    def create_resources(cls, directory, file_name):
        """Create resources based on the directory and file name."""
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, file_name), "w") as f:
            f.write("This is a sample file.")

    @classmethod
    def cleanup(cls, directory, file_name):
        """Clean up resources created."""
        os.remove(os.path.join(directory, file_name))
        if not os.listdir(directory):
            os.rmdir(directory)

    @classmethod
    def execute_all(cls, file_name):
        """Execute all operations."""
        path = cls.get_path(file_name)
        directory, file_name = cls.parse_path()
        cls.create_resources(directory, file_name)
        cls.cleanup(directory, file_name)
        return f"Operations executed successfully for file: {file_name}"

# Testing the methods
print(FileOperations.execute_all("test_file2.txt"))
