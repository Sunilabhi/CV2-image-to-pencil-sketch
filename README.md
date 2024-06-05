# PencilSketcher App

This Web App helps convert your photos to realistic Pencil Sketches using OpenCV and Streamlit.

## Features

- Upload a photo in JPEG, JPG, or PNG format
- Convert the uploaded photo to a pencil sketch
- View the original and the pencil sketch images
- Download the pencil sketch image

## Requirements

- Python 3.6 or higher
- Streamlit
- OpenCV
- Pillow (PIL)

## Installation

1. Clone the repository or download the project files.

2. Create and activate a virtual environment (optional but recommended).

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, you can manually install the dependencies:

    ```bash
    pip install streamlit opencv-python pillow
    ```

## Usage

1. Run the Streamlit app.

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the sidebar to upload your photo.

4. View the original photo and the generated pencil sketch.

5. Click the "Download Pencil Sketch" button to download the sketch.

