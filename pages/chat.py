import streamlit as st
import openai
from utils import load_openai_api

openai.api_key = load_openai_api()

if "history" not in st.session_state:  # 初始化對話紀錄
    st.session_state.history = []  # 對話紀錄

if "system_message" not in st.session_state:  # 初始化系統訊息
    st.session_state.system_message = "你只能回答中文，請使用繁體中文回答我。"

    if "model" not in st.session_state:  # 初始化模型
        st.session_state.model = "gpt-4o-2024-08-06"

col1, col2, col3 = st.columns([4, 2, 1])

with col1:
    st.session_state.system_message = st.text_input(
        "系統訊息", value=st.session_state.system_message
    )

with col2:
    st.session_state.model = st.selectbox(
        "AI模型",
        [
            "gpt-4o-mini",
            "gpt-4o-2024-08-06",
        ],
    )

with col3:
    if st.button("🗑️"):
        st.session_state.history = []
        st.rerun()

for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪄").write(message["content"])
    else:
        st.chat_message("assistant", avatar="✨").write(message["content"])

prompt = st.chat_input("請輸入想要對話的訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model=st.session_state.model,
        temperature=0.7,
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + [{"role": "user", "content": prompt}],
    )
    assistant_massage = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": assistant_massage})
    st.rerun()
