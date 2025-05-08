from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import pytesseract
import io

app = FastAPI()

# Set the path if Tesseract is not in your PATH environment variable
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Example path for MacOS/Linux
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Example path for Windows

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png", "image/tiff"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG, PNG, and TIFF are supported.")
    
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        text = pytesseract.image_to_string(image)
        return {"extracted_text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
