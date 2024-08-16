import random

print("歡迎來到猜數字遊戲！")
print("我已經想好了一個1到100之間的數字。")

ans = random.randint(1, 100)
max = 100
min = 1
while True:  # 無窮迴圈
    # 可以把想要測試的數字寫在try中，如果程式碼有誤，就會執行except裡的程式碼
    # try跟except是一對的，最少要有一個try，一個except，也可以有多個except
    try:
        num = int(input(f"猜一個數字（{min}到{max}之間）："))  # 輸入數字
    except:  # 如果輸入的數字不是數字
        print("請輸入1-100之間的數字！")
        continue  # 跳出這次迴圈，進入下一次迴圈

    if num < 0 or num > 100:  # 如果超出範圍
        print("請輸入1-100之間的數字！")

    elif num < ans:  # 如果輸入小於答案
        print("太小了，再大一點！")
        if num < max_num:  # 檢查num是否大於max_num
            max_num = num  # 如果num大於max_num就跟新範圍

    elif num > ans:  # 如果超出範圍
        print("太大了，再小一點！")
        if num > max_num:  # 檢查num是否小於max_num
            max_num = num  # 如果num小於max_num就跟新範圍
    else:
        print(f"恭喜你！你猜中了數字 {number_to_guess}。")
