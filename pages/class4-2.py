import random

print("歡迎來到猜數字遊戲！")
print("我已經想好了一個1到100之間的數字。")

number_to_guess = random.randint(1, 100)

while True:
    guess = int(input("猜一個數字（1到100之間）："))

if guess < 0:
    print("請輸入1-100之間的數字！")

elif guess > 100:
    print("請輸入1-100之間的數字！")

elif guess < number_to_guess:
    print("太小了，再大一點！")
elif guess > number_to_guess:
    print("太大了，再小一點！")
else:
    print(f"恭喜你！你猜中了數字 {number_to_guess}。")
