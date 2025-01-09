import csv
import os
import aiofiles

from fastapi import HTTPException

CSV_FILE = "data/data.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "upload_time"])

async def csv_update(filename, upload_time):
    """
    Update (Create/Append) a new entry to the CSV file asynchronously.

    Args:
        filename (str): The name of the uploaded file.
        upload_time (str): The upload time in ISO format.

    Raises:
        HTTPException: If an error occurs while updating the CSV file.
    """
    try:
        async with aiofiles.open(CSV_FILE, mode="a", newline="") as csv_file:
            # Write the row directly as a formatted string
            await csv_file.write(f"{filename},{upload_time}\n")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error updating the CSV") from e

def csv_read():
    """
    Read (Retrieve) the contents of the CSV file and return a list of dictionaries.

    Returns:
        list: A list of dictionaries with file data.

    Raises:
        HTTPException: If an error occurs while reading the CSV file.
    """
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            return [{"filename": row["filename"], "upload_time": row["upload_time"]} for row in reader]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error reading the CSV") from e

def csv_delete(filename):
    """
    Delete an entry from the CSV file based on the filename.

    Args:
        filename (str): The name of the file to remove from the CSV.

    Raises:
        HTTPException: If an error occurs while updating the CSV file.
    """
    try:
        rows = []
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[0] != filename]

        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error updating the CSV") from e
