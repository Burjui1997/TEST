"""
2. Написать функцию, которая принимает на вход два целых
числа (минимум и максимум) и возвращает список всех простых
чисел в заданном диапазоне.
"""


def prime_numbers(minimum, maximum):
    prime_list = []
    for i in range(minimum, maximum + 1):
        try:
            if i < 1:
                raise ValueError("Число должно быть больше 0")
        except ValueError as e:
            print(e)
            break
        if i == 1:
            continue
        if i > 1:
            for p in range(2, i):
                if i % 2 == 0:
                    break
                elif i % p == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


minimum = int(input("Введите минимальное число: "))
maximum = int(input("Введите максимальное число: "))

print(prime_numbers(minimum, maximum))
