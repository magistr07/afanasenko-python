'''
вариант 2
Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей. Определить, сколько стоит 1 кг шоколадных конфет, 
1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.
'''

X = float(input("Введите количество килограммов шоколадных конфет (X): "))
A = float(input("Введите стоимость X килограммов шоколадных конфет (A): "))
Y = float(input("Введите количество килограммов ирисок (Y): "))
B = float(input("Введите стоимость Y килограммов ирисок (B): "))

cost_per_kg_chocolate = A / X
cost_per_kg_toffee = B / Y
price_ratio = cost_per_kg_chocolate / cost_per_kg_toffee

print(f"Стоимость 1 кг шоколадных конфет: {cost_per_kg_chocolate:.2f} рублей")
print(f"Стоимость 1 кг ирисок: {cost_per_kg_toffee:.2f} рублей")
print(f"Шоколадные конфеты дороже ирисок в {price_ratio:.2f} раз")
