# gpb_server/cli/app.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from datetime import datetime
from gpb_server.utils import image_io, data_io
import uvicorn

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """
    Create (Upload) an image file and update the CSV with the file's information.

    Args:
        file (UploadFile): The image file to be uploaded.

    Returns:
        dict: A success message with the uploaded file's name.
    """
    # Log the received file information
    print(f"Received file: {file.filename}")

    # Save the image using the image_create function
    try:
        await image_io.image_create(file)  # Await the async function to save the image asynchronously
        print(f"File {file.filename} uploaded successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")
        raise HTTPException(status_code=500, detail="Error saving the file")

    # Update the CSV file
    try:
        await data_io.csv_update(file.filename, datetime.utcnow().isoformat())  # Add 'await' here
        print(f"File entry added to CSV: {file.filename}")
    except Exception as e:
        print(f"Error updating CSV: {e}")
        raise HTTPException(status_code=500, detail="Error updating the CSV")

    return {"message": f"File {file.filename} uploaded successfully!"}

@app.get("/images/")
def list_images():
    """
    Read (Retrieve) the list of all uploaded images from the CSV file.

    Returns:
        dict: A dictionary containing a list of images with filenames and upload times.
    """
    images = data_io.csv_read()
    return {"images": images}

@app.get("/images/{filename}")
def download_image(filename: str):
    """
    Read (Retrieve) a specific image by filename and return it for download.

    Args:
        filename (str): The name of the file to download.

    Returns:
        FileResponse: The image file for download.
    """
    file_path = image_io.image_read(filename)
    return FileResponse(file_path, media_type="image/jpeg", filename=filename)

@app.delete("/images/{filename}")
def delete_image(filename: str):
    """
    Delete an image file and remove its entry from the CSV file.

    Args:
        filename (str): The name of the file to delete.

    Returns:
        dict: A success message confirming deletion.
    """
    image_io.image_delete(filename)
    data_io.csv_delete(filename)
    return {"message": f"File {filename} deleted successfully!"}




import requests

def test():    
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        print("Response JSON:", response.json())
    else:
        print("Failed to fetch data. Status Code:", response.status_code)


def run():
    print("Your App is running... at http://127.0.0.1:8000/docs")
    test()
    # Run the application using Uvicorn, specify host as '127.0.0.1' for local access
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    run()
