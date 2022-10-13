# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в
# N-мерном пространстве.


def SpaceMeter():
    Diff = 0
    for i in range(N):
        List_Coordinate_A.append(int(input('Input the coordinate A ')))
        List_Coordinate_B.append(int(input('Input the coordinate B ')))
        Diff += (List_Coordinate_B[i] - List_Coordinate_A[i]) ** 2
    S = Diff ** 0.5
    print(S)


try:
    N = int(input('Please input the number of dimensions in space '))
    List_Coordinate_A = []
    List_Coordinate_B = []
    SpaceMeter()
except:
    print('Please input according of input conditions!')
