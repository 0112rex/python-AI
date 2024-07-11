i = 0
while i < 5:
    print(i)
    i=i+1 # i = i + 1

    #算術指定運算子
    a = 10
    a += 1 #等同於 a = a + 1
    a -= 1 #等同於 a = a - 1
    a *= 2 #等同於 a = a * 2
    a /= 2 #等同於 a = a / 2
    a %= 2 #等同於 a = a % 2
    a **= 2 #等同於 a = a ** 2
   
   # 根據以上符號列出優先順序
# 1. ()
# 2. **
# 3.* / // %
# 4.+ -
# 5== != > < >= <=
# 6 not and or
#7. = += -= *= /= %= **=

# break 跳出一層迴圈
while i  < 6: #條件式迴圈
    print(i)#印出i
    if i == 3: 
        break #如果i等於3,就跳出一層迴圈
    i += 1

   for i in range(1, 6):#for 迴圈
    print(i)
    if i == 3: 
        break #如果i等於3,就跳出一層迴圈

# random
import random #引入random模組
print(random.randint(10)) #產生一個0到10的隨機數
print(random.randint(1, 10)) #產生一個1到10的隨機數
print(random.randint(1, 10, 2)) #產生一個1到10的隨機數,每次產生2個數
#randrange跟range一樣,第一個數字是開始數,第二個數字是結束數,第三個數字是間隔
#不會數數到結束的數字,randrange(1,10)只會產生1到9的數字

print(random.randrange(1, 10)) #產生一個1到10的隨機數
#randint跟randrange一樣,第一個數字是開始數,第二個數字是結束數
#但randint一定要設定兩個數字，且會數到結束的數字

# 字串