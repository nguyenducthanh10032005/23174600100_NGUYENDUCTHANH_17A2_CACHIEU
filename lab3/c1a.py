n = int(input("Nhập 1 số nguyên dương n: "))  
S1 = 0
if n <= 0:
    print("n phải là số nguyên dương. Nhập lại.")
else:
    for i in range(1, n + 1):
        S1 += i
    print("Tổng S1 =", S1)
