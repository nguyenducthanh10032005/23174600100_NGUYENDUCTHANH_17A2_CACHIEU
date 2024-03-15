a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))

a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))

# Tính định thức của ma trận hệ số
Định_thuc_ma_tran_he_so = a1 * b2 - a2 * b1

# Tính nghiệm x và y
x = (b2 * c1 - b1 * c2) / Định_thuc_ma_tran_he_so
y = (a1 * c2 - a2 * c1) / Định_thuc_ma_tran_he_so

# In kết quả làm tròn đến hai chữ số sau dấu phẩy
print("Kết quả:")
print("x =", round(x, 2))
print("y =", round(y, 2))