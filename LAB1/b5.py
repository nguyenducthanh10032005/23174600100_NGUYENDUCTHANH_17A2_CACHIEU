def tinh_tien_dien(h):
    # Tính năng lượng tiêu thụ (kWh)
    nang_luong = 220 * 1.5 * h / 1000

    # Tính số tiền điện phải trả
    tien_dien = nang_luong * 5000

    return tien_dien

# Nhập số giờ sử dụng máy lọc không khí
so_gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))

# Tính và hiển thị tổng số tiền điện phải trả
tong_tien_dien = tinh_tien_dien(so_gio_su_dung)
print("Tổng số tiền điện phải trả: ", tong_tien_dien, "đồng")