print({})  # 空字典
print({"星期一": "蘋果"})
print({1: "蘋果", 2: "香蕉"})

# 讀取字典
d = {"星期一": "蘋果", "星期二": "香蕉"}
# key可重複
print(d["星期一"])  # 蘋果


# 字典的方法
d = {"星期一": "蘋果", "星期二": "香蕉"}
for key in d:  # 如果直接將字典當作迴圈翻為，預設會印出所有的key
    print(key)

for key in d.key():  # 可以使用key()方法印出所有的key
    print(key)
# 以上兩種方法可以同時印出所有的key

for value in d.values():
    print(value)

for key, value in d.items():  # 可以同時印出所有的key和value
    print(key, value)

for key, value in d.items():
    print(f"key={key},value={value}")

    for key, value in d.items():  # 取出所有的key和value，分別存入兩個變數
        print(f"key={key},value={value}")

# 元素新增/修改
d = {"星期一": "蘋果", "星期二": "香蕉"}
d["星期一"] = "橘子"
d["星期三"] = "蘋果"  # 新增元素，當key不存在時，會加入新元素
print(d)

# 檢查key是否存在
d = {"星期一": "蘋果", "星期二": "香蕉"}
# key有沒有在字典中
print("星期一" in d)  # True
print("星期三" in d)  # False
# value有沒有在字典中
print("蘋果" in d.values())  # True
print("香蕉" in d.values())  # True
l = ["星期一", "星期二"]
print("星期一" in l)  # True
print("星期三" in l)  # False

# 刪除元素
del d["星期一":"蘋果", "星期二":"香蕉"]
d.pop("星期一")
print(d)
d.pop("星期三", "找不到")
print(d)
