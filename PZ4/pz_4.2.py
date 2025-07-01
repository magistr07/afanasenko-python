'''
вариант 2
Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа, 
расположенные между A и B (не включая числа A и B), а также количество N этих чисел.
'''

A = int(input("Введите число A (A < B): "))
B = int(input("Введите число B (A < B): "))

if A >= B:
    print("Ошибка: A должно быть меньше B.")
else:
    numbers = list(range(A + 1, B))
    
    for number in reversed(numbers):
        print(number)

    N = len(numbers)
    print("Количество чисел между A и B:", N)
