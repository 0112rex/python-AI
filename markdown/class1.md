print("Hello, Streamlit!")

# Python 程式基礎筆記

## 印出文字與註解

```python
print("hello")  # 這適應出hello在終端機
print("56498")  # 這適應出56498在終端機
'''
這是多行註解
'''

print(123)  # 整數
print(True)  # 布林值
print(False)  # 布林值
print('"')  # 印出雙引號
print("'")  # 印出單引號
a = 1000
print(1 + 1)  # 加法
print(2 - 1)  # 減法
print(2 * 1)  # 乘法
print(2 / 1)  # 除法
print(2 // 1)  # 取整除法
print(2 ** 1)  # 次方計算
print(2 % 1)  # 取餘數計算
a = "hello"
b = "world"
print(a + " " + b * 3)  # 字串相加與乘法
print(f"hello{10}{True}")  # 字串格式化
print(len("hello"))  # 字串長度
print(int(123))  # 字串轉整數
print(float(123.456))  # 字串轉浮點數
print(bool(1))  # 整數轉布林值

print("input()可以在終端機輸入文字")
a = input("在這輸入文字: ")  # 可以在終端機輸入文字
print(f"你輸入的內容是: {a}")  # 印出輸入文字
print(f"你輸入的內容類型是: {type(a)}")  # 輸入的內容類型是字串
a = input("輸入正方形的邊長:")
area = int(a) * int(a)
print(f"正方形的面積是 {area}")
