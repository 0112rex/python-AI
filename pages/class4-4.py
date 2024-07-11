import streamlit as st
import os

st.title("圖片元件")
image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

image_size = st.number_input(
    "圖片大小", min_value=50, max_value=500, value=100, step=50
)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
