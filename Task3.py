# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки
# в другой.

def CountMatches():
    count = 0
    for i in range(len(String_1)):
        if String_1[i: (i + len(String_2))] == String_2:
            count += 1
    print(count)

def CountMatches2():
    count = 0
    for i in range(len(String_2)):
        if String_2[i: (i + len(String_1))] == String_1:
            count += 1
    print(count)

try:
    String_1 = input('Please input a string № 1 ')
    String_2 = input('Please input a string № 2 ')
    
    if String_1 >= String_2:
        CountMatches()
    else:
        CountMatches2()
except:
    print('Somthing was wrong!')

