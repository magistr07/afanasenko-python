...
Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
информацию из строки в словарь, найти среднее арифметическое оценок,
результаты вывести на экран.
...


data = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"

parts = data.split()

surname = parts[0]
name = parts[1]
group = parts[2]
grades = list(map(int, parts[3:]))

average_grade = sum(grades) / len(grades)

result = {
    "Фамилия": surname,
    "Имя": name,
    "Группа": group,
    "Оценки": grades,
    "Средний балл": average_grade
}

print(result)
