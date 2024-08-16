import streamlit as st
import openai
from utils import load_openai_api

openai.api_key = load_openai_api()

prompt_text = st.text_area("prompt", "    ")
if st.button("開始生成圖片"):
    generatedImage = openai.images.generate(model="dall-e-3", prompt=prompt_text, n=1)
    image_url = generatedImage.data[0].url
    st.image(image_url)
