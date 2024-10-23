# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()

    number_of_letters = 0
    dict_of_letters = {}

    for letter in text:
        if letter.isalpha():
            number_of_letters += 1
            dict_of_letters[letter] = 0
    for letter in dict_of_letters:
        dict_of_letters[letter] = text.count(letter)

    return [dict_of_letters, number_of_letters]


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_of_letters, number_of_letters):
    for letter in dict_of_letters:
        dict_of_letters[letter] = dict_of_letters[letter] / number_of_letters

    return dict_of_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_of_letters = calculate_frequency(count_letters(main_str)[0], count_letters(main_str)[1])

for letter in dict_of_letters:
    print(f"{letter}:", "%.2f" % dict_of_letters[letter])
