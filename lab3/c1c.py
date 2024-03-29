import math
n = int(input("Nhập số nguyên dương n: "))
S3 = 0
if n > 0:
    for i in range(1, n+1):
        S3 += 1 / math.sqrt(2 * i)
    print("Tổng S3 =", S3)
else:
    print("n phải là số nguyên dương. Nhập lại.")
