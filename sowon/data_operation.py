import csv
from typing import List, Dict, Union
from pathlib import Path
import json

class SingletonMeta(type):
    """A metaclass for implementing the Singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class FileManager(metaclass=SingletonMeta):
    """Handles basic file I/O operations."""

    def read(self, file_path: str) -> str:
        """Reads the contents of a file as a string."""
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")

            return path.read_text(encoding="utf-8")
        except Exception as e:
            raise IOError(f"Error reading file: {file_path}. Details: {e}")

    def write(self, content: str, file_path: str) -> None:
        """Writes a string to a file."""
        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        except Exception as e:
            raise IOError(f"Error writing file: {file_path}. Details: {e}")


class TabularManager(metaclass=SingletonMeta):
    """Manages tabular data parsing and formatting."""

    def __init__(self):
        self.file_manager = FileManager()

    def read_csv(self, file_path: str) -> List[Dict[str, Union[str, int, float]]]:
        """Reads a CSV file and converts rows into JSON objects."""
        try:
            content = self.file_manager.read(file_path)
            reader = csv.DictReader(content.splitlines(), delimiter=",")
            return [dict(row) for row in reader]
        except Exception as e:
            raise ValueError(f"Error parsing CSV file: {file_path}. Details: {e}")

    def read_tsv(self, file_path: str) -> List[Dict[str, Union[str, int, float]]]:
        """Reads a TSV file and converts rows into JSON objects."""
        try:
            content = self.file_manager.read(file_path)
            reader = csv.DictReader(content.splitlines(), delimiter="\t")
            return [dict(row) for row in reader]
        except Exception as e:
            raise ValueError(f"Error parsing TSV file: {file_path}. Details: {e}")

    def write_tabular(
        self, data: List[Dict[str, Union[str, int, float]]], save_path: str, file_type: str
    ) -> None:
        """Writes JSON objects as a tabular file (CSV or TSV)."""
        try:
            if not data:
                raise ValueError("Data to write cannot be empty.")

            delimiter = "," if file_type.lower() == "csv" else "\t"
            header = data[0].keys()
            rows = [header] + [[row[key] for key in header] for row in data]

            content = "\n".join(
                delimiter.join(map(str, row)) for row in rows
            )
            self.file_manager.write(content, save_path)
        except Exception as e:
            raise ValueError(f"Error writing tabular file: {save_path}. Details: {e}")



# Singleton instances
tabular_manager = TabularManager()

# Reading a CSV file
csv_data = tabular_manager.read_csv("data.csv")
print(csv_data)



# Printing each JSON object in human-readable format
print("CSV Data in Human-Readable Format:")
for index, item in enumerate(csv_data, start=1):
    print(f"Row {index}:")
    print(json.dumps(item, indent=2))
    print()  # Add a blank line for better separation

# # Writing to a CSV file
# tabular_manager.write_tabular(csv_data, "output.csv", "csv")




# # Reading a TSV file
# tsv_data = tabular_manager.read_tsv("data.tsv")
# print(tsv_data)



# # Writing to a TSV file
# tabular_manager.write_tabular(tsv_data, "output.tsv", "tsv")
