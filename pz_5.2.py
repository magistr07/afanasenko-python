'''
2 варик
Описать функцию Mean(параметры), вычисляющую среднее арифметическое
AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух положительных 
'''

import random as r


def SortDec3(A, B, C):
    if A < B:
        A, B = B, A

    if B < C:
        B, C = C, B

    if A < B:
        A, B = B, A

    return A, B, C


A1, B1, C1 = r.randint(-50, 50), r.randint(-50, 50), r.randint(-50, 50)
print(f"Первый набор до сортировки: {A1}, {B1}, {C1}")
A1, B1, C1 = SortDec3(A1, B1, C1)
print(f"Первый набор после сортировки: {A1}, {B1}, {C1}")


A2, B2, C2 = r.randint(-50, 50), r.randint(-50, 50), r.randint(-50, 50)
print(f"Второй набор до сортировки: {A2}, {B2}, {C2}")
A2, B2, C2 = SortDec3(A2, B2, C2)
print(f"Второй набор после сортировки: {A2}, {B2}, {C2}")
