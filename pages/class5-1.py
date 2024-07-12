import streamlit as st
import time
import os

# 設計products字典，每個商品價格(price)和庫存(stock)圖片(image)

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
# products 範例
# products ={ "apple": {"price": 10, "stock": 10, "image": "apple.png"},
#         "banana": {"price": 10, "stock": 10, "image": "banana.png"},
#        "orange": {"price": 10, "stock": 10, "image": "orange.png"},
#        }

# 顯示商品
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
                st.erron(f"庫存不足")
    i += 1

# 新增商品庫存區塊
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
# 重新顯示商品以反映新增庫存
st.markdown("目前商品庫存：")
for product_name, details in st.session_state.products.items():
    st.markdown(f"{product_name}: {details['stock']}件")
