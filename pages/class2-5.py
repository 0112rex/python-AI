print([])  # 空的 list
print([1])  # 包含一個數字的 list
print(["蘋果"])  # 包含一個字串的 list
print(["a", "b"])  # 包含兩個字串的 list
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
