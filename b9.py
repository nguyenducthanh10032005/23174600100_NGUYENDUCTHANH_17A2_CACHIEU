def tinh_trung_diem(x1, y1, x2, y2):
    trung_diem_x = (x1 + x2) / 2
    trung_diem_y = (y1 + y2) / 2
    return trung_diem_x, trung_diem_y

# Nhập tọa độ của bốn đỉnh
x_m = float(input("Nhập tọa độ x của điểm M: "))
y_m = float(input("Nhập tọa độ y của điểm M: "))

x_n = float(input("Nhập tọa độ x của điểm N: "))
y_n = float(input("Nhập tọa độ y của điểm N: "))

x_p = float(input("Nhập tọa độ x của điểm P: "))
y_p = float(input("Nhập tọa độ y của điểm P: "))

x_q = float(input("Nhập tọa độ x của điểm Q: "))
y_q = float(input("Nhập tọa độ y của điểm Q: "))

# Tính toán và in ra tọa độ trung điểm của các cạnh
td_mn = tinh_trung_diem(x_m, y_m, x_n, y_n)
td_np = tinh_trung_diem(x_n, y_n, x_p, y_p)
td_pq = tinh_trung_diem(x_p, y_p, x_q, y_q)
td_qm = tinh_trung_diem(x_q, y_q, x_m, y_m)

print("Tọa độ trung điểm của cạnh MN là:", td_mn)
print("Tọa độ trung điểm của cạnh NP là:", td_np)
print("Tọa độ trung điểm của cạnh PQ là:", td_pq)
print("Tọa độ trung điểm của cạnh QM là:", td_qm)
