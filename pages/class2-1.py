print(1 == 1)  # 這是比較是否相等
print(1 != 2)  # 這是比較是否不相等
print(1 < 2)  # 這是比較是否小於
print(1 > 2)  # 這是比較是否大於
print(1 <= 2)  # 這是比較是否小於或等於
print(1 >= 2)  # 這是比較是否大於或等於

print(not True)  # 這是相反的運算
print(not False)  # 這是相反的運算

print(True and True)  # 這是全部要符合才算true
print(True and False)  # 這是全部要符合才算true
print(False and True)  # 這是全部要符合才算true
print(False and False)  # 這是全部要符合才算true

print(True or True)  # 這是全部要符合才算true
print(True or False)  # 這是全部要符合才算true
print(False or True)  # 這是全部要符合才算true
print(False or False)  # 這是全部要符合才算true


# 根據以上符號列出優先順序
# 1. ()
# 2. **
# 3.* / // %
# 4.+ -
# 5== != > < >= <=
# 6 not and or

pwd = input("請輸入密碼：")
if pwd == "123":
    print("密碼正確")
elif pwd == "1234":
    print("密碼正確")
else:
    print("密碼錯誤")
    # 判斷一定要是if 開頭，if只有一個
    # elif 可以有多個
    # 判斷可以有一個else，也可以沒有
    # else和elif都是選擇性的
