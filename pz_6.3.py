...
Дан список размера N. Обнулить элементы списка, расположенные между его 
минимальным и максимальным элементами (не включая минимальный и 
максимальный элементы).
...

def zero_between_min_max(lst):
    if len(lst) < 3:
        return lst

    min_idx = lst.index(min(lst))
    max_idx = lst.index(max(lst))

    left = min(min_idx, max_idx)
    right = max(min_idx, max_idx)
    
    for i in range(left + 1, right):
        lst[i] = 0
    
    return lst

N = int(input("Введите размер списка N: "))
my_list = []

print("Введите элементы списка:")
for i in range(N):
    element = int(input(f"Элемент {i+1}: "))
    my_list.append(element)

print("Исходный список:", my_list)
result = zero_between_min_max(my_list)
print("Результат:", result)
