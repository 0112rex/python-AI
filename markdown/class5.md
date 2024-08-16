
# Streamlit 應用程式筆記

## 1. 環境設置

```python
import streamlit as st
import time
import os
```

## 2. 設計產品字典

### 產品字典設計

設計 `products` 字典，每個商品包括價格、庫存和圖片。

```python
import_folder = "image"
image_files = os.listdir(import_folder)
if "products" not in st.session_state:
    st.session_state.products = {}

for image_file in image_files:
    product_name = image_file[:-4]
    if product_name not in st.session_state.products:
        st.session_state.products[product_name] = {
            "price": 10,
            "stock": 10,
            "image": f"{import_folder}/{image_file}",
        }
```

### 產品範例

```python
# products 範例
# products ={ 
#     "apple": {"price": 10, "stock": 10, "image": "apple.png"},
#     "banana": {"price": 10, "stock": 10, "image": "banana.png"},
#     "orange": {"price": 10, "stock": 10, "image": "orange.png"},
# }
```

## 3. 顯示商品

### 商品顯示

顯示商品的圖片、價格和庫存。

```python
st.title("購物平台")
col_num = st.number_input("欄數", min_value=1, value=2)
col = st.columns(col_num)
i = 0
for product_name, details in st.session_state.products.items():
    with col[i % col_num]:
        st.image(details["image"], use_column_width=True)
        st.markdown(f"### {product_name}")
        st.markdown(f"價格：{details['price']}")
        st.markdown(f"庫存：{details['stock']}")

        if st.button(f"購買{product_name}", key=f"{product_name}"):
            if details["stock"] > 0:
                st.session_state.products[product_name]["stock"] -= 1
                st.success(f"購購買 {product_name} 成功!")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"庫存不足")
    i += 1
```

## 4. 新增商品庫存

### 庫存新增

```python
st.title("新增商品庫存")
product_name = list(st.session_state.products.keys())
col1, col2 = st.columns(2)
with col1:
    selected_product = st.selectbox("選擇商品", product_name)
with col2:
    new_stock = st.number_input("新增庫存", min_value=1, step=1)
if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += new_stock
    st.success(f"{selected_product} 庫存已增加 {new_stock} 件")
    time.sleep(1)
    st.rerun()
```

### 目前庫存顯示

```python
st.markdown("目前商品庫存：")
for product_name, details in st.session_state.products.items():
    st.markdown(f"{product_name}: {details['stock']}件")
```

## 5. 函數定義與使用

### 定義與使用函數

```python
def hello():  
    print("Hello!")

hello()

def hello2(name):  
    print(f"Hello, {name}!")  

hello2("John")  
hello2("Ray")

def hello3(name, age):  
    print(f"Hello, {name}! You are {age} years old.")

hello3("John", 18)  
hello3("Ray", 20)  
hello3(age=20, name="Ray")

def age10(age):  
    return age + 10

print(age10(18))  
print(age10(20))

x = 10
print(f"x = {x}")  
if x > 5:
    x = 20

length = 5  
area = 3.14 * 10**2  

def calculate_square_area():  
    global area  
    area = length**2  
    a = 10  
    print("區域變數a是", a)  

calculate_square_area()  
print("面積是", area)
```

## 6. 使用 OpenAI API 進行對話

### 設置背景和 API 密鑰

```python
from utils import set_background

set_background("image/angry-man.png", 50, "center bottom")

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

col1, col2 = st.columns([4, 1])
with col1:
    openai_key = st.text_input("Password", type="password", key="password")
    if openai_key is None or openai_key == "":
        st.warning("請輸入OpenAI API Key")
        st.stop()
```

### 初始化對話紀錄

```python
if "history" not in st.session_state:  
    st.session_state.history = []  

with col2:
    if st.button("🗑️"):  
        st.session_state.history = []  
        st.rerun()  
```

### 顯示對話紀錄

```python
msgs = [
    HumanMessage("請用繁體中文進行後續對話")
]  
for actor, message in st.session_state.history:  
    if actor == "user":  
        st.chat_message("user", avatar="🪄").write(message)  
        msgs.append(HumanMessage(message))  
    else:
        st.chat_message("assistant", avatar="✨").write(
            message
        )  
        msgs.append(AIMessage(message))  
```

### 處理對話輸入

```python
chat = ChatOpenAI(model="gpt-4o", temperature=0.2, api_key=openai_key)
prompt = st.chat_input("請輸入想要對話的訊息")  
if prompt:  
    st.session_state.history.append(["user", prompt])  
    msgs.append(HumanMessage(prompt))  
    response = chat.invoke(msgs).content  
    st.session_state.history.append(
        ["assistant", response]
    )  
    st.rerun()
```
