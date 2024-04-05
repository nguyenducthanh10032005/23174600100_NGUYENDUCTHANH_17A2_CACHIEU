#4a
num = int(input("Nhập số nguyên: "))
count = 0
while num != 0:
    count += 1
    num //= 10
print("Số chữ số của số nguyên là:", count)
#4b
m = int(input("Nhập số nguyên m (m > 10): "))
a = 0
S2 = 0
while True:
    S2 = 1 / (3**(2*a+1))
    a += 1
    if S2 <= m:
        break
print("Các tổng S2:",S2)
