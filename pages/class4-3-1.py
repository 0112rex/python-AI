# 字典
# dist是透過key-value取得資料,key是唯一的,value可重複
# dist是無序的,所以無法透過index取得資料
# dist的key必須是不可變的資料型態
# dist的value可以是任意資料型態
# dist的key-value是透過冒號來連接的key和value
# dist的key-value之間用逗號隔開
d = {"a": 1, "b": 2, "c": 3}

# 取得dist中的key
print(d.keys())  # dist_keys(['a', 'b', 'c'])
for key in d.keys():  # dist_keys(['a', 'b', 'c'])
    print(key)  # a

# 取得dist中的value
print(d.values())  # dist_values([1, 2, 3])
for value in d.values():  # dist_values([1, 2, 3])
    print(value)  # 1

# 取得dist中的key-value
print(d.items())  # dist_items([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():  # dist_items([('a', 1), ('b', 2), ('c', 3)])
    print(key, value)  # a 1

# 新增 修改 dist的key-value
d["d"] = 4  # 新增
print(d)  # dist_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
d["b"] = 5  # 修改
print(d)  # dist_items([('a', 1), ('b', 5), ('c', 3), ('d', 4)])

# 檢查dist是否有某個key
# in不能檢查value
# 跟list比較,in可以檢查value的元素 dist的key
print("a" in d)  # True
print("e" in d)  # False

# 刪除dist中的key-value
# 如果資料存在,就刪除回傳value
print(d.pop("a"))  # 5
# 如果資料不存在,就刪除傳回預設值
print(d.pop("e", "not found"))  # not found
# 如果資料不存在也沒預設值,就報錯

# 比較複雜的dist
d = {
    "a": [1, 2, 3],
    "b": {"c": 4, "d": 5},
}

# 成績登記系統,key是學生名稱,value是成績,每個科目有3個成績
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 95, 100], "英文": [95, 90, 85]},
    "小美": {"國文": [80, 70, 60], "數學": [75, 85, 95], "英文": [70, 80, 90]},
    "小芳": {"國文": [70, 60, 50], "數學": [65, 75, 85], "英文": [60, 70, 80]},
}
# 取得小明的數學成績
print(grade["小明"]["數學"])  # [85, 95, 100]
# 取得小美第一次英文成績
print(grade["小美"]["英文"][0])  # 70
# 取得小芳第二次國文成績

# 印出每位學的國文段考平均成績
for name, subjects in grade.items():
    # 取得國文成績
    chinese = subjects["國文"]
    # 計算平均成績
    avg = sum(chinese) / len(chinese)
    print(f"{name}的國文平均成績為{avg:.2f}")

# 印出每位學的總平均成績
for name, subjects in grade.items():
    total = 0
    for score in subjects.values():
        total += sum(score)
    avg = total / (len(subjects) * 3)
    print(f"{name}的總平均成績為{avg:.2f}")

# 整理全校各科目的平均成績
# 建立一個dist用來存儲每個科目的成績
avg_grade = {"國文": [], "數學": [], "英文": []}
# 逐一取得每位學生的成績
for subjects in grade.values():  # 取得每位學生的各科目成績
    # subjects={"國文": [90, 80, 70], "數學": [85, 95, 100], "英文": [95, 90, 85]}
    # 逐一取得每個科目的成績
    for subject, scores in subjects.items():
        # scores=[90, 80, 70]
        # 將各科成績加入avg_grade
        avg_grade[subject] + -scores
print(avg_grade)
# avg_grade={
#'國文': [90, 80, 70, 80, 70, 60, 70, 60, 50],
#'數學': [85, 95, 100, 75, 85, 65, 75, 85, 65],
#'英文': [95, 90, 85, 70, 80, 60, 70, 80, 60],
# }

# 印出每位學的國文段考平均成績
for name, subjects in grade.items():
    # 取得國文成績
    chinese = subjects["國文"]
    # 計算平均成績
    avg = sum(chinese) / len(chinese)
    print(f"{name}的國文平均成績為{avg:.2f}")
