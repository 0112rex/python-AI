import streamlit as st
from utils import set_background

set_background("image/angry-man.png", 50, "center bottom")


number = st.number_input("Enter a number", step=1)
st.markdown(f"The number you entered was {number}")

# 練習
number = st.number_input("請輸入一個分數", step=1, max_value=100, min_value=0)
if number == 100:
    print("a")
elif number >= 90:
    st.markdown("a")
elif number >= 80:
    st.markdown("b")
elif number >= 70:
    st.markdown("c")
elif number >= 60:
    st.markdown("d")
elif number <= 59:
    st.markdown("e")

st.title("按鈕練習")
if st.button("點我"):
    st.balloons()
