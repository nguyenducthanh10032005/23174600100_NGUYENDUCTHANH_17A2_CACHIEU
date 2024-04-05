import math

def main():
    while True:
        # Nhập hai số từ bàn phím
        try:
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
            continue
        
        # Thực hiện các phép tính
        print("Kết quả:")
        print("  +:", num1 + num2)
        print("  -:", num1 - num2)
        print("  *:", num1 * num2)
        if num2 != 0:
            print("  /:", num1 / num2)
        else:
            print("  /: Không thể chia cho 0.")
        print("  ^:", num1 ** num2)
        if num1 >= 0:
            print("  √:", math.sqrt(num1))
        else:
            print("  √: Không thể tính căn bậc hai của số âm.")

        # Hỏi người dùng có muốn tiếp tục không
        choice = input("Bạn có muốn tiếp tục không? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
