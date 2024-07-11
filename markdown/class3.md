## 程式技巧筆記

### List 操作

#### 建立 List

```python
L = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]  # 這是一個有10個元素的list
```

#### 增加元素

```python
L.append(8)  # 把8加到L的最後面
```

#### 計算元素個數

```python
c = L.count(3)  # 計算L中有幾個3
```

#### 移除元素

```python
for i in range(c):  # 把L中的所有3都移除
    L.remove(3)
```

#### 使用 `pop` 和 `remove`

```python
L.pop(0)  # 把L中的第0個元素移除
```

```python
# pop 與 remove 的差別
# pop 是用index, remove 是用元素來刪除
```

#### 排序

```python
L.sort()  # 把L中的元素由小到大排序
L.sort(reverse=True)  # 把L中的元素由大到小排序
```

#### 找出元素的 index

```python
print(L.index(5))  # 找出L中的5的index
```

### Streamlit 操作

#### 建立標題

```python
st.title("欄位元件")
```

#### 建立欄位

```python
col1, col2 = st.columns(2)  # 2欄
```

#### 建立按鈕

```python
col1.button("按鈕1")  # 在col1中建立一個按鈕
col2.button("按鈕2")  # 在col2中建立一個按鈕
```

#### 在欄位中增加元件

```python
with col1:
    st.markdown("這是欄1")
    st.button("左邊按鈕")
with col2:
    st.markdown("這是欄2")
    st.button("右邊按鈕")
```

#### 自訂欄位比例

```python
cols = st.columns([1, 5, 1])  # 3欄, list中的數字代表比例為1:5:1
cols[0].button("按鈕1", key="button1")  # 在第0欄中建立一個按鈕
cols[1].button("按鈕2", key="button2")  # 在第1欄中建立一個按鈕
cols[2].button("按鈕3", key="button3")  # 在第2欄中建立一個按鈕
```

#### 建立文字輸入框

```python
st.title("文字輸入框")
text = st.text_input("請輸入文字")  # 建立一個文字輸入框
st.markdown(f"你輸入的文字是{text}")
```

#### 使用 `session_state`

```python
st.title("session_state")
ans = 1
st.markdown(f"##### {ans}")
if st.button("按鈕", key="btn"):  # 如果按鈕被按下, 頁面會重新執行
    ans += 1  # ans = ans + 1,
st.markdown(f"##### {ans}")  # 這時候ans會是2, 不會變成3或以上, 因為頁面重新執行時ans會重新設定為1
```

#### 初始化 `session_state` 變數

```python
if "ans" not in st.session_state:  # 如果session_state中沒有ans這個變數
    st.session_state.ans = 1  # 建立一個ans的狀態變數, 設定為1
```

#### 更新 `session_state` 變數

```python
if st.button("session_state按鈕", key="session_state_btn"):  # 如果按鈕被按下, 頁面會重新執行
    st.session_state.ans += 1  # session_state中的ans加1, 這時候ans可以持續增加
st.markdown(f"##### {st.session_state.ans}")
```

#### 頁面重新整理

```python
import time

if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面
```

#### 建立點餐機介面

```python
st.title("點餐機")

if "order" not in st.session_state:
    st.session_state.order = []  # 新增一個購物車的list

col1, col2 = st.columns(2)  # 2欄
with col1:
    foodInput = st.text_input("請輸入餐點")  # 建立一個文字輸入框

with col2:
    if st.button("加入", key="add"):  # 如果按鈕被按下
        st.session_state.order.append(foodInput)  # 把餐點加到購物車

st.write(f"### 購物籃")
for i in range(len(st.session_state.order)):  # 用index來取得購物車中的餐點
    col1, col2 = st.columns(2)  # 2欄
    with col1:
        st.write(st.session_state.order[i])  # 顯示餐點

    with col2:
        if st.button("刪除", key=i):  # 如果按鈕被按下, key是index
            st.session_state.order.pop(i)
            # 把購物車中的餐點移除,這時候不能用remove,因為remove是用元素來刪除, 因為可能會刪除錯誤的餐點
            st.rerun()  # 重新整理整個頁面
```
