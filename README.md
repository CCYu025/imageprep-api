# Image Preprocess API + GUI

A simple Flask-based image processing API with a Streamlit GUI frontend. This project allows users to upload images, apply transformations (e.g., grayscale, blur, edge detection), and download the processed results.

## 🚀 Features

- **Multiple image processing modes**:
    - Grayscale conversion
    - Resize (200×200)
    - Edge detection (Canny)
    - Blur (Gaussian)
    - Sharpen
    - Rotate (90° clockwise)
    - Flip horizontally / vertically
    - Color inversion
- **Flask API**:
    - `POST /process-image` accepts an image file and mode parameter
    - Returns processed image in JPEG or PNG format
- **Streamlit GUI**:
    - Intuitive web interface for selecting mode and previewing results
    - Download button for saving processed images
- **Cross-Origin Resource Sharing** via `flask-cors`
- **Unit tests** with pytest for all modes and error cases
- **Docker-ready** for easy deployment

## 📦 Tech Stack

- Python 3.10+
- Flask
- OpenCV (opencv-python)
- NumPy
- Pillow
- Flask-Cors
- Streamlit
- Requests
- Gunicorn (production WSGI server)
- pytest (testing)

## 📋 Requirements

Dependencies are listed in `requirements.txt`:

```
flask==3.1.1
flask-cors>=4.0.0
opencv-python==4.11.0.86
Pillow==10.2.0
numpy==2.2.0
gunicorn>=21.2.0
streamlit>=1.0.0
requests>=2.25.0
pytest>=6.0.0

```

Install with:

```bash
pip install -r requirements.txt

```

## 🔧 Installation & Setup

1. Clone the repository:
    
    ```bash
    git clone https://github.com/your-repo/image-preprocess-api.git
    cd image-preprocess-api
    
    ```
    
2. (Optional) Create and activate a virtual environment:
    
    ```bash
    python -m venv .venv
    source .venv/bin/activate    # macOS/Linux
    .\.venv\\Scripts\\activate # Windows
    
    ```
    
3. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    

## 🚀 Running Locally

### 1. Start the Flask API

```bash
export FLASK_APP=app.py       # macOS/Linux
set FLASK_APP=app.py          # Windows
flask run --host 0.0.0.0 --port 5000

```

API will be available at `http://localhost:5000/process-image`.

### 2. Launch Streamlit GUI

```bash
streamlit run image_preprocess_ui.py

```

Open the displayed URL (usually `http://localhost:8501`) in your browser.

## 🛠 API Usage

**Endpoint**: `POST /process-image`

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | file | Image file to process (JPEG, PNG, GIF) |
| `mode` | string | Processing mode (see list above) |

**Example** with `curl`:

```bash
curl -X POST http://localhost:5000/process-image \
  -F "file=@path/to/image.jpg" \
  -F "mode=blur" --output result.jpg

```

## ✅ Running Tests

```bash
pytest -q

```

## 🐳 Docker

Build and run with Docker:

```bash
docker build -t image-preprocess-api .
docker run -p 5000:5000 image-preprocess-api

```

For UI, run:

```bash
docker run -p 8501:8501 image-preprocess-api streamlit run image_preprocess_ui.py

```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m "Add YourFeature"
4. Push to branch: `git push origin feature/YourFeature`
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

*Happy coding!*