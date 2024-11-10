# TODO Найдите количество книг, которое можно разместить на дискете
inf_volume_Mb = 1.44  # Объем в Мб
inf_volume_B = inf_volume_Mb * 1024 * 1024 # Объем в байтах
num_str = 100   # Количество страниц
num_strings = 50    # Количество строк на странице
num_char = 25   # Количество символов в строке
inf_char = 4    # Объем одного символа
num_books = int(inf_volume_B // (num_str * num_strings * num_char * inf_char))

print("Количество книг, помещающихся на дискету:", num_books)
