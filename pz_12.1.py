import random

n = int(input("Введите чётное количество элементов последовательности А: "))
while n % 2 != 0:
    n = int(input("Ошибка! Число должно быть чётным. Введите снова: "))

A = [random.randint(-10, 10) for _ in range(n)]
print("\nПоследовательность A:", A)

B = A[:n//2] 
C = A[n//2:]  
print("Последовательность B (первая половина):", B)
print("Последовательность C (вторая половина):", C)

product_sequence = [b * c for b, c in zip(B, C)]
print("\nПроизведение соответствующих элементов B и C:", product_sequence)

average = sum(product_sequence) / len(product_sequence)
print("\nСреднее арифметическое полученной последовательности:", average)

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f"Последовательность A: {A}\n")
    f.write(f"Последовательность B (первая половина): {B}\n")
    f.write(f"Последовательность C (вторая половина): {C}\n")
    f.write(f"Произведение соответствующих элементов: {product_sequence}\n")
    f.write(f"Среднее арифметическое: {average}\n")

print("\nРезультаты сохранены в файл 'result.txt'")
