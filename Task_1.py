# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
#  Через строку нельзя решать.
# *Пример:*

# - 6782,0 -> 23
# - 0,56 -> 11


def Sum_of_Digits(n):

    n *= 1000000000000
    n = int(n)
    Sum = 0

    while n >= 1:
        Sum = Sum + int(n%10)
        n = n//10 
    print(f'сумма = {Sum}')

try:
    n = float(input('Please input a digit '))
    Sum_of_Digits(n)
except:
    print('Please input a digits only!')












