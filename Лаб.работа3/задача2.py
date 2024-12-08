def find_common_participants(participants_str1, participants_str2, separator=","):
    group1 = participants_str1.split(separator)
    group2 = participants_str2.split(separator)
    common = sorted(list(set(group1) & set(group2)))  # Используем множества для эффективного поиска пересечения
    return common
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(f"Общие участники: {common_participants}")

participants_first_group_2 = "Иванов,Петров,Сидоров"
participants_second_group_2 = "Петров,Сидоров,Смирнов"
common_participants_2 = find_common_participants(participants_first_group_2, participants_second_group_2)
print(f"Общие участники (с запятой): {common_participants_2}")