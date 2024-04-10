"""
4. Написать программу, которая сортирует список строк по длине,
сначала по возрастанию, а затем по убыванию.
"""


def sort_length(string):
    sort_asc = sorted(string, key=len)
    sort_desc = sorted(string, key=len, reverse=True)
    return sort_asc, sort_desc


string = ["Я", "ХОЧУ", "БЫТЬ", "ПРОГРАММИСТОМ", "УСТАЛ", "ОТ", "МЕДИЦИНЫ"]
print(sort_length(string))