chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
chuoi_tron = ''
a = 0
while a < len(chuoi_1) or a < len(chuoi_2):
    if a < len(chuoi_1):
        chuoi_tron += chuoi_1[a]
    if a < len(chuoi_2):
        chuoi_tron += chuoi_2[a]
    if a < min(len(chuoi_1), len(chuoi_2)) - 1:
        chuoi_tron += '-'
    a += 1
print("Chuỗi sau khi trộn:", chuoi_tron)
