...
Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником.
...
import pickle

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return self.average_grade() >= 4.5

    def __str__(self):
        return f"{self.last_name} {self.first_name}, средний балл: {self.average_grade():.2f}, отличник: {'да' if self.is_excellent() else 'нет'}"

def save_def(students, filename="students.dat"):
    with open(filename, "wb") as file:
        pickle.dump(students, file)
    print(f"Данные сохранены в файл {filename}")

def load_def(filename="students.dat"):
    try:
        with open(filename, "rb") as file:
            students = pickle.load(file)
        print(f"Данные загружены из файла {filename}")
        return students
    except FileNotFoundError:
        print("Файл не найден!")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        return []

student1 = Student("Иван", "Иванов", [5, 5, 5, 5])
student2 = Student("Петр", "Петров", [4, 5, 4, 5])
student3 = Student("Сергей", "Сергеев", [3, 4, 3, 4])

students_list = [student1, student2, student3]

print("Созданные студенты:")
for student in students_list:
    print(student)

save_def(students_list)

loaded_students = load_def()

print("\nЗагруженные студенты:")
for student in loaded_students:
    print(student)
