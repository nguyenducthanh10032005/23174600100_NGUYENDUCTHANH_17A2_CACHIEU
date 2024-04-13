def can_transform_string(str1, str2):
    # Đếm số lượng ký tự khác nhau giữa hai chuỗi
    diff_count = abs(len(str1) - len(str2))

    # Nếu hai chuỗi có độ dài khác nhau quá nhiều thì không thể biến đổi thành chuỗi khác nhau bằng cách thêm hoặc xóa ký tự
    if diff_count > 1:
        return False

    # Đếm số lượng ký tự khác nhau từng vị trí giữa hai chuỗi
    mismatch_count = 0
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            mismatch_count += 1
            if mismatch_count > 1:
                return False
            # Nếu hai chuỗi có cùng độ dài, thì chỉ cần tăng chỉ số của cả hai chuỗi để so sánh tiếp
            if len(str1) == len(str2):
                i += 1
                j += 1
            # Nếu hai chuỗi có độ dài khác nhau, chỉ cần tăng chỉ số của chuỗi có độ dài lớn hơn để tiếp tục so sánh
            elif len(str1) > len(str2):
                i += 1
            else:
                j += 1
        else:
            i += 1
            j += 1

    return True

# Nhập chuỗi từ người dùng
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

# Kiểm tra xem có thể biến đổi chuỗi thứ nhất thành chuỗi thứ hai không
if can_transform_string(str1, str2):
    print("Có thể biến đổi chuỗi thứ nhất thành chuỗi thứ hai.")
else:
    print("Không thể biến đổi chuỗi thứ nhất thành chuỗi thứ hai.")
