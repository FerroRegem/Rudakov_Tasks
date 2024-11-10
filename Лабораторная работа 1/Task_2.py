# TODO Найдите количество книг, которое можно разместить на дискете
Inf_volume_Mb = 1.44  # Объем в Мб
Inf_volume_B = Inf_volume_Mb * 1024 * 1024 # Объем в байтах
Num_str = 100   # Количество страниц
Num_strings = 50    # Количество строк на странице
Num_char = 25   # Количество символов в строке
Inf_char = 4    # Объем одного символа
Num_books = int(Inf_volume_B // (Num_str * Num_strings * Num_char * Inf_char))

print("Количество книг, помещающихся на дискету:", Num_books)
