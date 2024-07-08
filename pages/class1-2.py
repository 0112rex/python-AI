import streamlit as st

st.title("這是標題")
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
st.markdown(
    """
這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊：
```python
print("Hello, Streamlit!")
```
"""
)


st.markdown(
    """
以下是將你提供的程式碼內容整理成 Markdown 筆記的格式：

```markdown
# Python 程式基礎筆記

## 印出文字與註解

```python
print("hello")  # 這適應出hello在終端機
print("56498")  # 這適應出56498在終端機
'''
這是多行註解
'''
```

## 印出不同型態的資料

```python
print(123)  # 整數
print(True)  # 布林值
print(False)  # 布林值
print('"')  # 印出雙引號
print("'")  # 印出單引號
```

## 數學運算與變數使用

```python
a = 1000
print(1 + 1)  # 加法
print(2 - 1)  # 減法
print(2 * 1)  # 乘法
print(2 / 1)  # 除法
print(2 // 1)  # 取整除法
print(2 ** 1)  # 次方計算
print(2 % 1)  # 取餘數計算
```

## 字串運算與格式化

```python
a = "hello"
b = "world"
print(a + " " + b * 3)  # 字串相加與乘法
print(f"hello{10}{True}")  # 字串格式化
print(len("hello"))  # 字串長度
```

## 型態轉換與使用者輸入

```python
print(int(123))  # 字串轉整數
print(float(123.456))  # 字串轉浮點數
print(bool(1))  # 整數轉布林值

print("input()可以在終端機輸入文字")
a = input("在這輸入文字: ")  # 可以在終端機輸入文字
print(f"你輸入的內容是: {a}")  # 印出輸入文字
print(f"你輸入的內容類型是: {type(a)}")  # 輸入的內容類型是字串
```

## 計算正方形面積範例

```python
a = input("輸入正方形的邊長:")
area = int(a) * int(a)
print(f"正方形的面積是 {area}")
```

這份筆記包含了 Python 的基本語法與技巧，包括變數使用、數學運算、字串操作、型態轉換以及使用者輸入處理。
"""
)
