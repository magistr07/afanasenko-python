import random

with open('исходные_данные.txt', 'w', encoding='utf-8') as file:
    numbers = [random.randint(-100, 100) for _ in range(20)]
    file.write(' '.join(map(str, numbers)))

with open('исходные_данные.txt', 'r', encoding='utf-8') as file:
    numbers = list(map(int, file.read().split()))

count = len(numbers)  
max_num = max(numbers) 

first_half = numbers[:len(numbers)//2]
product = 1
for num in first_half:
    if num < 0:
        product *= num
if product == 1:
    if any(num < 0 for num in first_half):
        pass 
    else:
        product = 0 
with open('результаты.txt', 'w', encoding='utf-8') as file:
    file.write("Исходные данные:\n")
    file.write(' '.join(map(str, numbers)) + '\n')
    file.write(f"Количество элементов: {count}\n")
    file.write(f"Максимальный элемент: {max_num}\n")
    file.write(f"Произведение элементов меньших 0 в первой половине: {product}\n")

print("Файлы успешно созданы!")
