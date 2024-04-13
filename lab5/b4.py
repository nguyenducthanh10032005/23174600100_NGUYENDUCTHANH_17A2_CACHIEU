def remove_non_digits(string):
    # Khởi tạo một chuỗi rỗng để lưu trữ ký tự số
    digits = ""
    for char in string:
        if char.isdigit():
            digits += char
    return digits

def is_prime(n):
    # Kiểm tra nếu n là số nguyên tố
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập chuỗi từ người dùng
string = input("Nhập chuỗi ký tự: ")

# Loại bỏ các ký tự không phải là số
digits_only = remove_non_digits(string)

# Kiểm tra nếu chuỗi ký tự kết quả là số nguyên tố
if digits_only:
    number = int(digits_only)
    if is_prime(number):
        print(f"Chuỗi ký tự {digits_only} là một số nguyên tố.")
    else:
        print(f"Chuỗi ký tự {digits_only} không phải là một số nguyên tố.")
else:
    print("Không có số nguyên tố trong chuỗi đã nhập.")

