n = int(input("Nhập số nguyên dương n: "))
S2 = 0
if n <= 0:
    print("Nhập lại n là số nguyên dương!")
else:
    for i in range(1, n + 1):
        S2 += 1 / i
    print("Tổng S2 =", S2)