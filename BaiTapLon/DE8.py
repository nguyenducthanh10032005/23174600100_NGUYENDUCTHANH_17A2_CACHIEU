import random
import csv

# Danh sách tên người tham gia
nguoi_tham_gia = [
    'Nguyen Van A', 'Le Thi B', 'Tran Van C', 'Pham Thi D', 'Hoang Van E',
    'Vu Thi F', 'Dang Van G', 'Bui Thi H', 'Nguyen Thi I', 'Le Van J',
    'Tran Thi K', 'Pham Van L', 'Hoang Thi M', 'Vu Van N', 'Dang Thi O'
]

# Set lưu trữ những người đã được chia nhóm
da_chia_nhom = set()

# Dictionary lưu trữ các nhóm và thành viên của nhóm
nhom = {}

# Hàm chia ngẫu nhiên các người tham gia vào các nhóm
def chia_ngau_nhien(nguoi_tham_gia, so_nhom):
    random.shuffle(nguoi_tham_gia)
    nhom = {f'Group {i+1}': [] for i in range(so_nhom)}
    for i, nguoi in enumerate(nguoi_tham_gia):
        nhom[f'Group {(i % so_nhom) + 1}'].append(nguoi)
        da_chia_nhom.add(nguoi)
    return nhom

# Hàm tính xác suất một người được chia vào một nhóm cụ thể
def tinh_xac_suat(ten_nguoi, nhom, tong_so_nguoi):
    so_nhom = len(nhom)
    for group, members in nhom.items():
        if ten_nguoi in members:
            return 1 / so_nhom
    return 0

# Hàm hiển thị danh sách nhóm và thành viên trong mỗi nhóm
def hien_thi_nhom(nhom):
    for group, members in nhom.items():
        print(f'{group}: {", ".join(members)}')

# Hàm lưu kết quả chia nhóm vào file CSV
def luu_csv(nhom, filename='ket_qua_chia_nhom.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Ten nguoi tham gia', 'Nhom', 'Xac suat'])
        for group, members in nhom.items():
            for member in members:
                xac_suat = tinh_xac_suat(member, nhom, len(nguoi_tham_gia))
                writer.writerow([member, group, xac_suat])

# Chia ngẫu nhiên 15 người tham gia vào 5 nhóm (mỗi nhóm 3 thành viên)
so_nhom = 5
nhom = chia_ngau_nhien(nguoi_tham_gia, so_nhom)

# Hiển thị danh sách nhóm và thành viên trong mỗi nhóm
hien_thi_nhom(nhom)

# Lưu kết quả chia nhóm vào file CSV
luu_csv(nhom)