'''
вариант 2
Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить, 
имеются ли в записи числа N нечетные цифры. Если имеются, то вывести TRUE, если нет — вывести FALSE.
'''

def has_odd_digit(N):
    while N > 0:
        digit = N % 10  
        if digit % 2 != 0:  
            return True
        N //= 10  
    return False


N = int(input("Введите целое число N (>0): "))
if has_odd_digit(N):
    print("TRUE")
else:
    print("FALSE")
