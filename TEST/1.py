"""
1. Написать функцию, которая принимает на вход
список целых чисел и возвращает новый список,
содержащий только уникальные элементы из исходного списка
"""


def unique_numbers(user_input):
    unique_list = []
    for i in user_input:
        if user_input.count(i) == 1:
            unique_list.append(i)
    return unique_list


user_input = input("Введите числа через пробел : ")
print(unique_numbers(user_input))
