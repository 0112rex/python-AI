# 程式技巧筆記

## 比較運算

```python
print(1 == 1)  # 比較是否相等
print(1 != 2)  # 比較是否不相等
print(1 < 2)  # 比較是否小於
print(1 > 2)  # 比較是否大於
print(1 <= 2)  # 比較是否小於或等於
print(1 >= 2)  # 比較是否大於或等於
```

## 邏輯運算

```python
print(not True)  # 相反的運算
print(not False)  # 相反的運算

print(True and True)  # 全部要符合才算 True
print(True and False)  # 全部要符合才算 True
print(False and True)  # 全部要符合才算 True
print(False and False)  # 全部要符合才算 True

print(True or True)  # 任意一個符合就算 True
print(True or False)  # 任意一個符合就算 True
print(False or True)  # 任意一個符合就算 True
print(False or False)  # 任意一個符合就算 True
```

## 運算符號優先順序

1. `()`
2. `**`
3. `* / // %`
4. `+ -`
5. `== != > < >= <=`
6. `not and or`

## 條件判斷

```python
pwd = input("請輸入密碼：")
if pwd == "123":
    print("密碼正確")
elif pwd == "1234":
    print("密碼正確")
else:
    print("密碼錯誤")
# 判斷一定要是 if 開頭，if 只有一個
# elif 可以有多個
# 判斷可以有一個 else，也可以沒有
# else 和 elif 都是選擇性的
```

## 使用 Streamlit 建立網頁應用程式

```python
import streamlit as st

number = st.number_input("Enter a number", step=1)
st.markdown(f"The number you entered was {number}")

# 練習
number = st.number_input("請輸入一個分數", step=1, max_value=100, min_value=0)
if number == 100:
    st.markdown("a")
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
```

## 迴圈

```python
for i in range(10):  # i 是迴圈變數, range(10) 是從 0 開始到 9 的數字
    print(i)  # 每次從 range(10) 中印出一個數字

for i in range(2, 100):  # i 是迴圈變數, range(2, 100) 是從 2 開始到 99 的數字
    print(i)  # 每次從 range(2, 100) 中印出一個數字

for i in range(2, 10, 2):  # i 是迴圈變數, range(2, 10, 2) 是從 2 開始到 9 的數字, 每次取出的數字是偶數
    print(i)  # 每次從 range(2, 10, 2) 中印出一個數字

for i in range(100, 3, -2):  # range(100, 3, -2) 是從 100 開始到 3 的數字, 每次取出的數字是奇數
    print(i)  # 每次從 range(100, 3, -2) 中印出一個數字, 從 100 到 4 的偶數
```

## 列表操作

```python
print([])  # 空的 list
print([1])  # 包含一個數字的 list
print(['蘋果'])  # 包含一個字串的 list
print(['a', 'b'])  # 包含兩個字串的 list
print([1, 2, 3])  # 包含三個數字的 list

L = [1, 2, 3]
print(L[0])  # 取出 list 的第一個元素
print(L[1])  # 取出 list 的第二個元素
print(L[2])  # 取出 list 的第三個元素

for index in range(len(L)):
    print(L[index])  # 取出 list 的元素

for item in L:
    print(item)  # 迭代 list 的每個元素

L[0] = "moo"  # 把 list 的第一個元素改成 "moo"
```
