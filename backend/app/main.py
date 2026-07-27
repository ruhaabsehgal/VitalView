from fastapi import FastAPI, UploadFile, File
import shutil
from pathlib import Path

from app.services.pdf_service import extract_text_from_pdf
from app.services.report_parser import extract_parameters

app = FastAPI(
    title="VitalView API",
    version="1.0.0",
    description="Backend API for the VitalView application."
)

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@app.get("/")
def root():
    return {
        "message": "Welcome to the VitalView API!"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(file_path)

    # Parse important medical parameters
    parsed_report = extract_parameters(extracted_text)

    # Return response
    return {
    "message": "File uploaded successfully!",
    "filename": file.filename,
    "text": extracted_text,
    "report": parsed_report
}