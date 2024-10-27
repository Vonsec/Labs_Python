# TODO Напишите функцию find_common_participants
def find_common_participants(group1: str, group2: str, delimiter: str = ',') -> list:
    participants1 = set(group1.split(delimiter)) if group1 else set()
    participants2 = set(group2.split(delimiter)) if group2 else set()
    common_participants = participants1 & participants2
    return sorted(common_participants)


participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

common_participants_comma = find_common_participants(participants_first_group_comma, participants_second_group_comma)
print("Общие участники (разделитель ','):", common_participants_comma)

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники (разделитель '|'):", common_participants)
