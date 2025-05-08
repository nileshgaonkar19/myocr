
# OCR API Service with Tesseract and FastAPI

This project is an OCR (Optical Character Recognition) API service built with **FastAPI** and **Tesseract-OCR**. It allows you to upload image files and extracts the text content from them. Supported image formats include **JPEG**, **PNG**, and **TIFF**.

## Features
- ✅ Extract text from images using Tesseract
- ✅ Support for multiple image formats (JPEG, PNG, TIFF)
- ✅ Fast and asynchronous processing with FastAPI
- ✅ Swagger UI documentation for easy API testing

---

## Prerequisites

1. **Python 3.8+**
2. **Tesseract-OCR**

### Install Tesseract-OCR

#### Ubuntu:
```bash
sudo apt-get install tesseract-ocr
```

#### MacOS (using Homebrew):
```bash
brew install tesseract
```

#### Windows:
Download the installer from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract) and add it to your system PATH.

To verify the installation:
```bash
tesseract --version
```

---

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/ocr-api-service.git
cd ocr-api-service
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

Run the FastAPI application:
```bash
uvicorn main:app --reload
```

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI documentation for easy testing.

---

## API Endpoints

### `POST /extract-text/`
Uploads an image and extracts text from it.

#### Request:
- **file** (required): Image file (JPEG, PNG, TIFF)

#### Example using `cURL`:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/extract-text/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path_to_your_image.png'
```

#### Response:
```json
{
  "extracted_text": "This is the text extracted from the image."
}
```

---

## Environment Variables
If Tesseract is not in your PATH, you can specify it in `main.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Mac/Linux path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows path
```

---

## Docker Setup
You can easily run this application inside a Docker container.

### Build the Docker Image:
```bash
docker build -t ocr-api-service .
```

### Run the Docker Container:
```bash
docker run -d -p 8000:8000 ocr-api-service
```

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI.

---

## Contributing
Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

## License
MIT License

---

## Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/)
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
