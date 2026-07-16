from fastapi import FastAPI, UploadFile, File
import shutil
from pathlib import Path

app = FastAPI(
    title="VitalView API",
    version="1.0.0",
    description="Backend API for the VitalView application."
)

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Welcome to VitalView!",
        "status": "Backend is running"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully!",
        "filename": file.filename
    }