length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2


calculate_square_area()
print("面積是", area)  # 面積是100


length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2
    return area


area = calculate_square_area()
print("面積是", area)  # 面積是25


length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    global area  # 宣告area是全域變數
    area = length**2
    return area


calculate_square_area()
print("面積是", area)  # 面積是25
