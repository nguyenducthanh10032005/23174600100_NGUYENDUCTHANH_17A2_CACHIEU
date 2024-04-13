def find_word_positions(text, word):
    positions = []
    start = 0
    while True:
        start = text.find(word, start)
        if start == -1:
            break
        positions.append(start)
        start += 1
    return positions

def most_common_word(text):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    most_common = max(word_count, key=word_count.get)
    return most_common

# Nhập chuỗi văn bản từ người dùng
text = input("Nhập chuỗi văn bản: ")

# Nhập từ cần tìm kiếm từ người dùng
word_to_find = input("Nhập từ cần tìm kiếm: ")

# Tìm và hiển thị vị trí của từ trong chuỗi
positions = find_word_positions(text, word_to_find)
if positions:
    print("Vị trí của từ trong chuỗi:", positions)
else:
    print("Từ không được tìm thấy trong chuỗi.")

# Tìm và hiển thị từ xuất hiện nhiều nhất trong chuỗi
most_common = most_common_word(text)
print("Từ xuất hiện nhiều nhất trong chuỗi là:", most_common)
