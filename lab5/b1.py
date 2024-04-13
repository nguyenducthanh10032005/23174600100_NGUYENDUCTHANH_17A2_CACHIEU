so_thap_phan = float(input("Nhập số nguyên dương (số thập phân): "))
if so_thap_phan < 0:
    print("Nhập số nguyên dương.")
else:
    if so_thap_phan == 0:
        print("Số nhị phân tương ứng là: 0")
    else:
        nhi_phan = ''
        while so_thap_phan > 0:
            nhi_phan = str(so_thap_phan % 2) + nhi_phan
            so_thap_phan //= 2
        print("Số nhị phân tương ứng là:", nhi_phan)
