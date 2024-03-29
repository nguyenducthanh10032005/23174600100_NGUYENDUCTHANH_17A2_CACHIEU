B = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        B += i
print("Tổng các số chia hết cho 7 không chia hết cho 5 từ 2000 đến 4000 là:", B)

