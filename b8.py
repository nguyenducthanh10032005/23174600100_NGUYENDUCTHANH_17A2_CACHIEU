import math

def Tính_gtri_bthuc(x, z):
    a = (x ** 2 * math.sin(z) + math.sqrt(abs(x)))
    b = math.log(z) + math.exp(x - 1)
    c = a / b + math.atan(x * z)
    d = round(c, 2)
    return d

# Nhập giá trị x và z từ người dùng
x = float(input("Nhập giá trị của x: "))
z = float(input("Nhập giá trị của z: "))

# Tính giá trị của biểu thức f(x, z)
result = Tính_gtri_bthuc(x, z)

# In kết quả
print("Giá trị của biểu thức f(x, z) là:", result)
