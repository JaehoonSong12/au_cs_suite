# gpb_server.cli.app.py
import requests
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import csv
import os
from datetime import datetime
import uvicorn





app = FastAPI()

# Paths
IMAGES_DIR = "data/images"
CSV_FILE = "data/data.csv"

# Ensure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)

# Ensure CSV file exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "upload_time"])  # Write headers


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Log the received file information
    print(f"Received file: {file.filename}")

    # Save the image
    try:
        file_path = os.path.join(IMAGES_DIR, file.filename)
        print(f"Saving file to {file_path}")
        with open(file_path, "wb") as image_file:
            image_file.write(await file.read())
        print(f"File saved successfully: {file.filename}")
    except Exception as e:
        print(f"Error saving file: {e}")
        raise HTTPException(status_code=500, detail="Error saving the file")

    # Update the CSV file
    try:
        with open(CSV_FILE, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([file.filename, datetime.utcnow().isoformat()])
        print(f"File entry added to CSV: {file.filename}")
    except Exception as e:
        print(f"Error updating CSV: {e}")
        raise HTTPException(status_code=500, detail="Error updating the CSV")

    return {"message": f"File {file.filename} uploaded successfully!"}

@app.get("/images/")
def list_images():
    # Read filenames from the CSV file
    if not os.path.exists(CSV_FILE):
        raise HTTPException(status_code=404, detail="CSV file not found")

    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        images = [{"filename": row["filename"], "upload_time": row["upload_time"]} for row in reader]

    return {"images": images}

@app.get("/images/{filename}")
def download_image(filename: str):
    # Check if the file exists
    file_path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path, media_type="image/jpeg", filename=filename)

@app.delete("/images/{filename}")
def delete_image(filename: str):
    # Delete the image file
    file_path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    os.remove(file_path)

    # Remove the entry from the CSV file
    rows = []
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row[0] != filename]

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return {"message": f"File {filename} deleted successfully!"}



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