 ...
1. В двумерном списке найти минимальный и максимальные элементы.
 ...




matrix = [
    [5, 2, 9],
    [8, 1, 4],
    [3, 6, 7]
]

min_elem = matrix[0][0]
max_elem = matrix[0][0]

for row in matrix:
    for elem in row:
        if elem < min_elem:
            min_elem = elem
        if elem > max_elem:
            max_elem = elem

print("Минимальный элемент:", min_elem)  # 1
print("Максимальный элемент:", max_elem)  # 9
