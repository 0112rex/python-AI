import streamlit as st

from utils import set_background

set_background("image/angry-man.png", 50, "center bottom")


st.title("數字金字塔")
number = st.number_input("請輸入一個數(1-9)", step=1, max_value=9, min_value=1)
st.markdown("數字金字塔")
for i in range(1, number + 1):
    st.markdown(str(i) * i)

number = st.number_input("請輸入箭頭大小:", step=1, min_value=1)
arrow = ""
for i in range(1, number * 2, 2):
    arrow += " " * ((number * 2 - i) // 2) + "*" * i + "\n"
for i in range(number):
    arrow += " " * (number - 1) + "*" + "\n"
st.markdown(f"```\n箭頭金字塔:\n{arrow}\n```")
