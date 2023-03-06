import streamlit as st
from PIL import Image
from io import BytesIO
import base64
from mmdet.apis import init_detector, inference_detector
import mmcv

def predict(image):
    config_file = 'config.py'
    checkpoint_file = 'epoch_22.pth'
    model = init_detector(config_file, checkpoint_file, device='cpu')
    result = inference_detector(model, image)
    model.show_result(image, result, out_file='result.jpg')
    return 'result.jpg'

# Download the detected image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def detect_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    detected = Image.open(predict(upload))
    col2.write("Detected Image :wrench:")
    col2.image(detected)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download detected image", convert_image(detected), "detected.png", "image/png")

# Design Web
st.set_page_config(layout="wide", page_title="Page Object Detection")
st.write("## Detect page object from your image")
st.write(
    ":dog: Try uploading an image to detect page object. Full quality images can be downloaded from the sidebar.:grin:"
)
st.sidebar.write("## Upload and download :gear:")

# Main
col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    detect_image(upload=my_upload.name)
else:
    detect_image("./113.jpg")
