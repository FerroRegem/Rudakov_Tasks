# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, divisor=","):
    set1 = set(string1.split(divisor))
    set2 = set(string2.split(divisor))
    set3 = set1.intersection(set2)
    return list(set3)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
divisor = "|"

print(find_common_participants(participants_first_group, participants_second_group, divisor))

# TODO Провеьте работу функции с разделителем отличным от запятой
