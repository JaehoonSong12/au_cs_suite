import re
import csv

from typing import List, Dict, Union
from pathlib import Path
from datetime import datetime


class SingletonMeta(type):
    """A metaclass for implementing the Singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DateManager(metaclass=SingletonMeta):
    def __init__(self):
        self.patterns = [
            "%m/%d/%y",    # MM/dd/yy (e.g., 01/18/25)
            "%d-%m-%Y",    # dd-MM-yyyy (e.g., 18-01-2025)
            "%Y/%m/%d",    # yyyy/MM/dd (e.g., 2025/01/18)
            "%m/%d/%Y",    # MM/dd/yyyy (e.g., 01/18/2025)
            "%Y-%m-%d",    # yyyy-MM-dd (e.g., 2025-01-18)
            "%d/%m/%Y",    # dd/MM/yyyy (e.g., 18/01/2025)
            "%m-%d-%Y",    # MM-dd-yyyy (e.g., 01-18-2025)
            "%m.%d.%Y",    # MM.dd.yyyy (e.g., 01.18.2025)
            "%d.%m.%y"     # dd.MM.yy (e.g., 18.01.25)
        ]

    def get_day_of_week(self, date_str):
        normalized_date_str = self.normalize_date(date_str)
        for pattern in self.patterns:
            try:
                date = datetime.strptime(normalized_date_str, pattern)
                return date.strftime("%A")  # Return the full name of the day of the week
            except ValueError:
                continue
        return "Invalid date format."

    def normalize_date(self, date_str):
        parts = re.split(r'[/\-\.]', date_str)
        if len(parts) >= 3:
            parts[0] = parts[0].zfill(2)
            parts[1] = parts[1].zfill(2)
            separator = "-" if "-" in date_str else "." if "." in date_str else "/"
            return separator.join(parts)
        return date_str

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








def testDate():    
    date_manager = DateManager()
    date_inputs = [
        "01.21.2025",
        "01.23.2025",
        "01.24.2025",
        "01.26.2025"
    ]
    for date_input in date_inputs:
        print(f"Input: {date_input}")
        print("Day of the week:", date_manager.get_day_of_week(date_input))



# Example usage:
if __name__ == "__main__":
    testDate()