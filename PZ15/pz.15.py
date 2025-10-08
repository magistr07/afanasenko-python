...
Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
выбранная Специальность.
...

import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect("abiturient.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Анкета (
            reg_number INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            birth_date TEXT NOT NULL,
            has_awards TEXT CHECK(has_awards IN ('да', 'нет')),
            address TEXT NOT NULL,
            specialty TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_abiturient(last_name, first_name, middle_name, birth_date, has_awards, address, specialty):
    try:
        if not all([last_name, first_name, birth_date, address, specialty]):
            print("Ошибка: Заполните все обязательные поля!")
            return False
        
        datetime.strptime(birth_date, '%Y-%m-%d')
        
        if has_awards.lower() not in ['да', 'нет']:
            print("Ошибка: Награды - 'да' или 'нет'")
            return False
        
        conn = sqlite3.connect("abiturient.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Анкета VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
        ''', (last_name, first_name, middle_name, birth_date, has_awards.lower(), address, specialty))
        conn.commit()
        conn.close()
        print("Абитуриент добавлен!")
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def view_all():
    conn = sqlite3.connect("abiturient.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Анкета")
    rows = cursor.fetchall()
    
    if not rows:
        print("Нет данных")
    else:
        for row in rows:
            print(f"№{row[0]}: {row[1]} {row[2]} {row[3]}, {row[4]}, Награды: {row[5]}, Адрес: {row[6]}, Специальность: {row[7]}")
    conn.close()

def search():
    print("\n1. По фамилии\n2. По специальности\n3. По наградам")
    choice = input("Выбор: ")
    
    conn = sqlite3.connect("abiturient.db")
    cursor = conn.cursor()
    
    if choice == "1":
        name = input("Фамилия: ")
        cursor.execute("SELECT * FROM Анкета WHERE last_name LIKE ?", (f"%{name}%",))
    elif choice == "2":
        spec = input("Специальность: ")
        cursor.execute("SELECT * FROM Анкета WHERE specialty = ?", (spec,))
    elif choice == "3":
        awards = input("Награды (да/нет): ")
        cursor.execute("SELECT * FROM Анкета WHERE has_awards = ?", (awards,))
    else:
        print("Неверный выбор")
        return
    
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"№{row[0]}: {row[1]} {row[2]}, {row[6]}")
    else:
        print("Не найдено")
    conn.close()

def delete():
    print("\n1. По номеру\n2. По ФИО\n3. Без наград")
    choice = input("Выбор: ")
    
    conn = sqlite3.connect("abiturient.db")
    cursor = conn.cursor()
    
    if choice == "1":
        num = input("Рег. номер: ")
        cursor.execute("DELETE FROM Анкета WHERE reg_number = ?", (num,))
    elif choice == "2":
        last = input("Фамилия: ")
        first = input("Имя: ")
        cursor.execute("DELETE FROM Анкета WHERE last_name = ? AND first_name = ?", (last, first))
    elif choice == "3":
        cursor.execute("DELETE FROM Анкета WHERE has_awards = 'нет'")
    else:
        print("Неверный выбор")
        return
    
    print(f"Удалено записей: {cursor.rowcount}")
    conn.commit()
    conn.close()

def edit():
    print("\n1. Адрес\n2. Специальность\n3. Награды")
    choice = input("Выбор: ")
    
    conn = sqlite3.connect("abiturient.db")
    cursor = conn.cursor()
    
    if choice == "1":
        num = input("Рег. номер: ")
        new_addr = input("Новый адрес: ")
        cursor.execute("UPDATE Анкета SET address = ? WHERE reg_number = ?", (new_addr, num))
    elif choice == "2":
        num = input("Рег. номер: ")
        new_spec = input("Новая специальность: ")
        cursor.execute("UPDATE Анкета SET specialty = ? WHERE reg_number = ?", (new_spec, num))
    elif choice == "3":
        num = input("Рег. номер: ")
        new_awards = input("Награды (да/нет): ")
        cursor.execute("UPDATE Анкета SET has_awards = ? WHERE reg_number = ?", (new_awards, num))
    else:
        print("Неверный выбор")
        return
    
    print("Данные обновлены")
    conn.commit()
    conn.close()

def add_samples():
    samples = [
        ("Иванов", "Иван", "Иванович", "2000-05-15", "да", "ул. Ленина, 123", "Информатика"),
        ("Петров", "Петр", "Петрович", "2001-03-20", "нет", "ул. Мира, 45", "Математика"),
        ("Сидорова", "Мария", "Сергеевна", "2000-11-10", "да", "пр. Победы, 67", "Физика"),
        ("Кузнецов", "Алексей", "Владимирович", "2001-07-03", "нет", "ул. Садовая, 89", "Информатика"),
        ("Смирнова", "Елена", "Дмитриевна", "2000-12-25", "да", "ул. Центральная, 12", "Химия"),
        ("Попов", "Дмитрий", "Александрович", "2001-02-14", "нет", "пр. Ленина, 34", "Математика"),
        ("Васильева", "Ольга", "Игоревна", "2000-09-08", "да", "ул. Школьная, 56", "Биология"),
        ("Новиков", "Сергей", "Олегович", "2001-06-30", "нет", "ул. Молодежная, 78", "Информатика"),
        ("Морозова", "Анна", "Викторовна", "2000-04-18", "да", "пр. Строителей, 90", "Физика"),
        ("Лебедев", "Андрей", "Николаевич", "2001-01-05", "нет", "ул. Парковая, 11", "Математика")
    ]
    
    for data in samples:
        add_abiturient(*data)

def main():
    create_database()
    
    while True:
        print("\n1. Добавить\n2. Просмотреть\n3. Поиск\n4. Удалить\n5. Редактировать\n6. Примеры\n7. Выход")
        choice = input("Выберите: ")
        
        if choice == "1":
            data = [
                input("Фамилия: "),
                input("Имя: "),
                input("Отчество: "),
                input("Дата рождения (ГГГГ-ММ-ДД): "),
                input("Награды (да/нет): "),
                input("Адрес: "),
                input("Специальность: ")
            ]
            add_abiturient(*data)
        elif choice == "2":
            view_all()
        elif choice == "3":
            search()
        elif choice == "4":
            delete()
        elif choice == "5":
             edit()
        elif choice == "6":
            add_samples()
        elif choice == "7":
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()
