# TODO заменить значение пропущенного элемента средним арифметическим

lost_el = 0
sum = 0

for i in range(len(numbers)):
    if numbers[i] is None:
        lost_el = i
    else:
        sum += numbers[i]

numbers[lost_el] = sum / len(numbers)


print("Измененный список:", numbers)
