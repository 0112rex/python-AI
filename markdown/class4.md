# 程式技巧筆記

## while 迴圈

```python
i = 0
while i < 5:
    print(i)
    i = i + 1  # i += 1
```

- **while 迴圈**：當條件為真時，持續執行內部的程式碼塊。
- **i += 1**：等同於 i = i + 1，增加 i 的值。

## 算術指定運算子

```python
a = 10
a += 1  # 等同於 a = a + 1
a -= 1  # 等同於 a = a - 1
a *= 2  # 等同於 a = a * 2
a /= 2  # 等同於 a = a / 2
a %= 2  # 等同於 a = a % 2
a **= 2  # 等同於 a = a ** 2
```

- 這些運算子用來對變數進行運算並賦值。

## 運算符號優先順序

1. `()`：括號
2. `**`：次方
3. `*` `/` `//` `%`：乘法、除法、整數除法、取餘數
4. `+` `-`：加法、減法
5. `==` `!=` `>` `<` `>=` `<=`：比較運算
6. `not` `and` `or`：邏輯運算
7. `=` `+=` `-=` `*=` `/=` `%=` `**=`：賦值運算

## break 跳出一層迴圈

```python
i = 0
while i < 6:  # 條件式迴圈
    print(i)
    if i == 3:
        break  # 如果 i 等於 3，就跳出一層迴圈
    i += 1
```

- **break**：跳出當前的迴圈。

## for 迴圈

```python
for i in range(1, 6):  # for 迴圈
    print(i)
    if i == 3:
        break  # 如果 i 等於 3，就跳出一層迴圈
```

- **for 迴圈**：遍歷序列（例如列表、範圍等）。

## random 模組

```python
import random  # 引入 random 模組

print(random.randint(0, 10))  # 產生一個 0 到 10 的隨機數
print(random.randint(1, 10))  # 產生一個 1 到 10 的隨機數
print(random.randrange(1, 10))  # 產生一個 1 到 9 的隨機數
```

- **randint(a, b)**：返回 a 到 b 之間的隨機整數，包含 a 和 b。
- **randrange(a, b)**：返回 a 到 b 之間的隨機整數，不包含 b。

## 字典操作

```python
# 創建字典
d = {"星期一": "蘋果", "星期二": "香蕉"}

# 讀取字典
print(d["星期一"])  # 蘋果

# 字典的方法
for key in d:  # 預設會印出所有的 key
    print(key)

for key in d.keys():  # 使用 key() 方法印出所有的 key
    print(key)

for value in d.values():  # 使用 values() 方法印出所有的 value
    print(value)

for key, value in d.items():  # 使用 items() 方法同時印出所有的 key 和 value
    print(f"key={key}, value={value}")

# 新增/修改元素
d["星期一"] = "橘子"
d["星期三"] = "蘋果"  # 新增元素
print(d)

# 檢查 key 是否存在
print("星期一" in d)  # True
print("星期三" in d)  # False

# 刪除元素
del d["星期一"]
d.pop("星期二")
print(d)
```

## streamlit 模組

```python
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
```

- **streamlit**：用於快速創建 web 應用的 Python 模組。
- **os 模組**：提供了訪問作業系統功能的介面。
