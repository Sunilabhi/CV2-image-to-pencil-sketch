import streamlit as st
import numpy as np
from PIL import Image
import cv2
from io import BytesIO

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return final_img

def convert_to_bytes(img):
    """Convert a NumPy array to bytes for download."""
    im_pil = Image.fromarray(img)
    buf = BytesIO()
    im_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

st.title("PencilSketcher App")
st.write("This Web App is to help convert your photos to realistic Pencil Sketches")

file_image = st.sidebar.file_uploader("Upload your Photos", type=['jpeg', 'jpg', 'png'])

if file_image is None:
    st.write("You haven't uploaded any image file")
else:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    st.write("**Input Photo**")
    st.image(input_img, use_column_width=True)
    st.write("**Output Pencil Sketch**")
    st.image(final_sketch, use_column_width=True)

    # Convert final sketch to bytes
    img_bytes = convert_to_bytes(final_sketch)
    
    # Download button
    st.download_button(
        label="Download Pencil Sketch",
        data=img_bytes,
        file_name="pencil_sketch.png",
        mime="image/png"
    )
