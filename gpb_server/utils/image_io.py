# gpb_server/utils/image_io.py

import os
from fastapi import UploadFile
from typing import Union
from fastapi import HTTPException

IMAGES_DIR = "data/images"

# Ensure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)

async def image_create(file: UploadFile):
    """
    Create (save) an image file to the server.

    This function receives an image file and saves it to the server.
    It is an async function to ensure non-blocking behavior when dealing with file operations.
    """
    try:
        file_path = os.path.join(IMAGES_DIR, file.filename)

        # Ensure the file is read asynchronously and saved to the server
        with open(file_path, "wb") as image_file:
            image_data = await file.read()  # Await the read operation
            image_file.write(image_data)
        print(f"File saved successfully: {file.filename}")
    except Exception as e:
        print(f"Error saving file: {e}")
        raise Exception("Error saving the file")

def image_delete(filename):
    """
    Delete an image file from the designated images directory.

    Args:
        filename (str): The name of the file to be deleted.

    Raises:
        HTTPException: If the file is not found or an error occurs while deleting the file.
    """
    file_path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    os.remove(file_path)

def image_read(filename):
    """
    Read (Retrieve) the file path for a given image filename.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The path to the image file.

    Raises:
        HTTPException: If the file is not found.
    """
    file_path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return file_path
