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
    conn = sqlite3.connect("abiturient.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO Анкета (last_name, first_name, middle_name, birth_date, has_awards, address, specialty)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (last_name, first_name, middle_name, birth_date, has_awards, address, specialty))
    
    conn.commit()
    conn.close()
    print("Абитуриент успешно добавлен!")

def view_all_abiturients():
    conn = sqlite3.connect("abiturient.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Анкета")
    rows = cursor.fetchall()
    
    if not rows:
        print("Нет данных об абитуриентах.")
    else:
        print("\nСписок абитуриентов:")
        for row in rows:
            print(f"""
            Рег. номер: {row[0]}
            ФИО: {row[1]} {row[2]} {row[3]}
            Дата рождения: {row[4]}
            Награды: {row[5]}
            Адрес: {row[6]}
            Специальность: {row[7]}
            """)
    
    conn.close()

def search_abiturient(last_name):
    conn = sqlite3.connect("abiturient.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Анкета WHERE last_name LIKE ?", (f"%{last_name}%",))
    rows = cursor.fetchall()
    
    if not rows:
        print("Абитуриент не найден.")
    else:
        print("\nРезультаты поиска:")
        for row in rows:
            print(f"""
            Рег. номер: {row[0]}
            ФИО: {row[1]} {row[2]} {row[3]}
            Дата рождения: {row[4]}
            Награды: {row[5]}
            Адрес: {row[6]}
            Специальность: {row[7]}
            """)
    
    conn.close()

def main():
    create_database()
    
    while True:
        print("\n--- Приложение АБИТУРИЕНТ ---")
        print("1. Добавить абитуриента")
        print("2. Просмотреть всех абитуриентов")
        print("3. Найти абитуриента по фамилии")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            print("\nВведите данные абитуриента:")
            last_name = input("Фамилия: ")
            first_name = input("Имя: ")
            middle_name = input("Отчество (если нет, нажмите Enter): ")
            birth_date = input("Дата рождения (ГГГГ-ММ-ДД): ")
            has_awards = input("Наличие наград (да/нет): ").lower()
            address = input("Адрес: ")
            specialty = input("Специальность: ")
            
            add_abiturient(last_name, first_name, middle_name, birth_date, has_awards, address, specialty)
        
        elif choice == "2":
            view_all_abiturients()
        
        elif choice == "3":
            search_name = input("Введите фамилию для поиска: ")
            search_abiturient(search_name)
        
        elif choice == "4":
            print("Выход из программы.")
            break
        
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
