...
Дан список размера N. Найти номера тех элементов список, которые больше своего 
левого соседа, и количество таких элементов. Найденные номера выводить в 
порядке их убывания. 
...

def find_elements_greater_than_left(lst):
    result_indices = []
    
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            result_indices.append(i)
    
    result_indices.sort(reverse=True)
    
    print("Номера элементов (в порядке убывания):", result_indices)
    print("Количество таких элементов:", len(result_indices))
    
    return result_indices

N = int(input("Введите размер списка N: "))
my_list = []

print("Введите элементы списка:")
for i in range(N):
    element = int(input(f"Элемент {i+1}: "))
    my_list.append(element)

print("Исходный список:", my_list)
find_elements_greater_than_left(my_list)
