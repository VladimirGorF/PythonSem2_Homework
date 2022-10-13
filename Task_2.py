# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Multiple_List(N):
    list = []
    x = 1
    for i in range(N):
        list.append(x)
        x += 1

    for i in range(2, N):
        list[i] = list[i] * list[i - 1]
    print(list)


try:
    N = int(input('Please input number N '))
    Multiple_List(N)
except:
    print('Please input an integer!')
