# TODO Найдите количество книг, которое можно разместить на дискете

total_volume = 1.44 * 2 ** 20
number_of_shapes = 100
number_of_strings = 50
number_of_symbols = 25
weight_of_one_symbol = 4

weight_of_one_book = number_of_shapes * number_of_strings * number_of_symbols * weight_of_one_symbol

number_of_books = int(total_volume // weight_of_one_book)

print("Количество книг, помещающихся на дискету:", number_of_books)
