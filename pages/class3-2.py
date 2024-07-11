import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 2欄
col1.button("按鈕1")  # 在col1中建立一個按鈕
col2.button("按鈕2")  # 在col2中建立一個按鈕
with col1:  # 在col1中任意增加元件
    st.markdown("這是欄1")
    st.button("左邊按鈕")
with col2:  # 在col2中任意增加元件
    st.markdown("這是欄2")
    st.button("右邊按鈕")

cols = st.columns([1, 5, 1])  # 3欄, list中的數字代表比例為1:5:1
cols[0].button("按鈕1", key="button1")  # 在第0欄中建立一個按鈕
cols[1].button("按鈕2", key="button2")  # 在第1欄中建立一個按鈕
cols[2].button("按鈕3", key="button3")  # 在第2欄中建立一個按鈕

st.title("文字輸入框")
text = st.text_input("請輸入文字")  # 建立一個文字輸入框
st.markdown(f"你輸入的文字是{text}")


st.title("session_state")
ans = 1
st.markdown(f"##### {ans}")
if st.button("按鈕", key="btn"):  # 如果按鈕被按下, 頁面會重新執行
    ans += 1  # ans = ans + 1,
st.markdown(
    f"##### {ans}"
)  # 這時候ans會是2, 不會變成3或以上, 因為頁面重新執行時ans會重新設定為1

if "ans" not in st.session_state:  # 如果session_state中沒有ans這個變數
    st.session_state.ans = 1  # 建立一個ans的狀態變數, 設定為1

if st.button(
    "session_state按鈕", key="session_state_btn"
):  # 如果按鈕被按下, 頁面會重新執行
    st.session_state.ans += 1  # session_state中的ans加1, 這時候ans可以持續增加
st.markdown(f"##### {st.session_state.ans}")
