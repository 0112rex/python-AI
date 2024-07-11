L = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]  # 這是一個有10個元素的list

L.append(8)  # 把8加到L的最後面
print(L)  # 印出L

c = L.count(3)  # 計算L中有幾個3
for i in range(c):  # 把L中的所有3都移除
    L.remove(3)

print(L)  # 印出L


L.pop(0)  # 把L中的第0個元素移除
print(L)  # 印出L
# pop 與 remove 的差別, pop 是用index, remove 是用元素來刪除

L.sort()  # 把L中的元素由小到大排序
print(L)  # 印出L
L.sort(reverse=True)  # 把L中的元素由大到小排序
print(L)  # 印出L

print(L.index(5))  # 找出L中的5的index
