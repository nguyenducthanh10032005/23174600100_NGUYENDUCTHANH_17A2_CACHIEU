import math

def tinh_dien_tich_xung_quanh(canh_day, chieu_cao):
    # Tính diện tích xung quanh của hình chóp tứ giác đều
    dien_tich_xung_quanh = 4 * 0.5 * canh_day * chieu_cao
    return dien_tich_xung_quanh

def tinh_dien_tich_toan_phan(canh_day, chieu_cao):
    # Tính diện tích toàn phần của hình chóp tứ giác đều
    dien_tich_day = canh_day ** 2
    dien_tich_toan_phan = dien_tich_day + tinh_dien_tich_xung_quanh(canh_day, chieu_cao)
    return dien_tich_toan_phan

def tinh_the_tich(canh_day, chieu_cao):
    # Tính thể tích của hình chóp tứ giác đều
    the_tich = (1/3) * canh_day**2 * chieu_cao
    return the_tich

# Nhập độ dài cạnh đáy và chiều cao từ người dùng
canh_day = float(input("Nhập độ dài cạnh đáy của hình chóp: "))
chieu_cao = float(input("Nhập chiều cao của hình chóp: "))

# Tính và in ra kết quả
dien_tich_xung_quanh = tinh_dien_tich_xung_quanh(canh_day, chieu_cao)
dien_tich_toan_phan = tinh_dien_tich_toan_phan(canh_day, chieu_cao)
the_tich = tinh_the_tich(canh_day, chieu_cao)

print("Diện tích xung quanh của hình chóp là:", round(dien_tich_xung_quanh, 2))
print("Diện tích toàn phần của hình chóp là:", round(dien_tich_toan_phan, 2))
print("Thể tích của hình chóp là:", round(the_tich, 2))