import streamlit as st
from utils import set_background

set_background("image/angry-man.png", 50, "center bottom")

import openai
from utils import load_openai_api, encode_image

openai.api_key = load_openai_api()

st.title("圖片分析")
upioaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])

if upioaded_file:
    st.image(upioaded_file, caption="以上傳圖片", width=300)

    with open("temp_image.jpg", "wb") as f:
        f.write(upioaded_file.getbuffer())

    base64_image = encode_image("temp_image.jpg")

    prompt = st.chat_input("請輸入想要對話的訊息")
    if prompt:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            },
                        },
                    ],
                },
            ],
        )

        assistant_massage = response.choices[0].message.content
        st.write(assistant_massage)
