#1a
sum = 0
n = []
while sum <= 1000:
    a = int(input("Nhập số nguyên dương: "))
    if a % 2 != 0:
        n.append(a)
    sum += a
print("Các số lẻ nhập:")
for a in n:
    print(a)

#1b
sum = 0
n = []
while sum <= 1000:
    a = int(input("Nhập số nguyên dương: "))
    if a % 2 == 0:
        n.append(a)
    sum += a
print("Các số chẵn nhập:")
for a in n:
    print(a)

#1c
sum = 0
k = 0
while sum <= 1000:
    n = int(input("Nhập số nguyên dương: "))
    sum += n
    k += 1
print("Số lượng số nguyên đã nhập:", k)

