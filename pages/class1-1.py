print("heiio")  # 這適應出hello在終端機
print("56498")  # 這適應出56498在終端機
"""
這是多行註解
"""


print(123)  # 整數
# print(123.456)  # 浮點數
# print(123.456e-2)  # 浮點數
# print(123.456e+2)  # 浮點數
# print(123.456e12)  # 浮點數
# print(123.456e-12)  # 浮點數


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
print(2**1)  # 次方計算
print(2 % 1)  # 取餘數計算
a = 10  # 把10存到變數a的空間，=就是將右邊的的值存到左邊的變數

# 符號的優先順序
# 1. ()
# 2**
# 3* / // %
# 4+ -

# 字串運算
a = "hello"
b = "world"
a + b  # 字串加法
# 加法乘法混和
print(a + " " + b * 3)  # 字串相加

print(f"hello{10}{True}")
# 在字串前加F，可以在字串中加入變數

print(len("hello"))  # 字串長度
print(int(123))  # 字串轉整數
print(float(123.456))  # 字串轉浮點數
print(bool(1))  # 整數轉布林值


print("input()可以在終端機輸入文字")
a = input(在這輸入文字)  # 可以在終端機輸入文字
print(f"你輸入的內容是式:{a}")  # 印出輸入文字
print(f"你輸入的內容是式:{type(a)}")  # 輸入的內容是字串

# 計算正方形的面積
a = input("輸入正方形的邊長:")
aren = int(a) * int(a)
print(f"正方形的面積是{aren}")
