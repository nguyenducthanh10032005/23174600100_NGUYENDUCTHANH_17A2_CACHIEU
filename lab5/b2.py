str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")
Cái_ngắn_nhất = ""
for i in range(len(str1)):
    for j in range(len(str2)):
        k = 0
        while (i + k < len(str1) and j + k < len(str2) and str1[i + k] == str2[j + k]):
            k += 1
        if k > 0:
            a = str1[i:i+k]
            if Cái_ngắn_nhất == "" or len(Cái_ngắn_nhất) < len(Cái_ngắn_nhất):
                Cái_ngắn_nhất = a
print("Chuỗi ký tự con chung ngắn nhất là:", Cái_ngắn_nhất)


