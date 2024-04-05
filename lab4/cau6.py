def main():
    # Dictionary ánh xạ từ số nguyên sang từ tiếng Anh tương ứng
    number_words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    # Nhập một số từ bàn phím
    number = input("Nhập một số: ")

    # Chuyển số thành từ tiếng Anh và in ra màn hình
    result = ''
    for digit in number:
        result += number_words.get(digit, '') + ' '
    print("Kết quả in ra màn hình là:", result.strip())

if __name__ == "__main__":
    main()
