# TODO Напишите функцию find_common_participants
def find_common_participants(list_of_members_1, list_of_members_2, sep=','):
    result_list = []

    list_of_members_1 = list_of_members_1.split(sep)
    list_of_members_2 = list_of_members_2.split(sep)

    for i in range(len(list_of_members_1)):
        if list_of_members_1[i] in list_of_members_2:
            result_list.append(list_of_members_1[i])

    result_list = sorted(result_list)
    return result_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, sep='|'))
