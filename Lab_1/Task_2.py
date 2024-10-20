# Исходные данные
disk_size_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4


disk_size_bytes = disk_size_mb * 1024 * 1024
total_chars_in_book = pages_per_book * lines_per_page * chars_per_line
book_size_bytes = total_chars_in_book * bytes_per_char
number_of_books = disk_size_bytes // book_size_bytes

# Результат
print("Количество книг, помещающихся на дискету:", int(number_of_books))

