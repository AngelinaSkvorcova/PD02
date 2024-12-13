# 6.uzd.

import = math
import random


def guess_the_number():

    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    print(
        f"Компьютер загадал число от {lower_bound} до {upper_bound}. Попробуйте угадать!")

    attempts = 0

    while True:
        user_guess = int(input("Введите ваше предположение: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("vairak!")
        elif user_guess > number_to_guess:
            print("mazak!")
        else:
            print(f"Pareizi! Загаданное число: {number_to_guess}")
            break

    print(f"Metienus skaits: {attempts}")


# 2 uzd.
n = int(input('ievadi skaitļu n: '))
summa = sum(range(1, n + 1))
print
# 3uzd.
n = int(input('ievadi skaitļi n:'))
print('!')(factorial)
n = 10
# 4uzd.
print('izvada_skaitļi n')
for i in range(n, -1,):
    else:
        print('10 < 0)
# 5 uzd.
height = int(input('ievadi height tristura'))
for i in range(height, 0, -5):
    print('*' * i)
