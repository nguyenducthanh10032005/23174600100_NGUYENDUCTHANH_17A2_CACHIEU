def count_special_characters(string):
    special_characters_count = {}
    total_characters = len(string)
    for char in string:
        if not char.isalnum():  # Kiểm tra xem ký tự có phải là ký tự đặc biệt không
            special_characters_count[char] = special_characters_count.get(char, 0) + 1
    
    return special_characters_count, total_characters

def calculate_percentage(count_dict, total):
    percentages = {}
    for char, count in count_dict.items():
        percentage = (count / total) * 100
        percentages[char] = percentage
    return percentages

# Nhập chuỗi từ người dùng
string = input("Nhập chuỗi ký tự: ")

# Đếm số lần xuất hiện của từng ký tự đặc biệt trong chuỗi và tỷ lệ phần trăm của mỗi ký tự đặc biệt
special_char_count, total_chars = count_special_characters(string)
percentages = calculate_percentage(special_char_count, total_chars)

# In kết quả
print("Số lần xuất hiện của từng ký tự đặc biệt trong chuỗi:")
for char, count in special_char_count.items():
    print(f"{char}: {count}")

print("\nTỷ lệ phần trăm của mỗi ký tự đặc biệt trong chuỗi:")
for char, percentage in percentages.items():
    print(f"{char}: {percentage:.2f}%")
