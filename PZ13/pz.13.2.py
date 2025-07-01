 ...
2. В двумерном списке отрицательные элементы возвести в квадрат.
 ...


matrix = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            matrix[i][j] **= 2  # Возводим в квадрат

print(matrix)
