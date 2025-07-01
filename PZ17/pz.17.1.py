import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    if not name_entry.get() or not email_entry.get() or not age_entry.get():
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все обязательные поля (*)")
        return
    
    data = {
        "Имя": name_entry.get(),
        "Телефон": phone_entry.get(),
        "Email": email_entry.get(),
        "Возраст": age_entry.get(),
        "Пол": gender_var.get(),
        "Личные качества": qualities_entry.get("1.0", tk.END).strip(),
        "Любимые животные": [animal for animal, var in animals_vars.items() if var.get()]
    }
    
    print("Форма отправлена:")
    for key, value in data.items():
        print(f"{key}: {value}")
    
    messagebox.showinfo("Успех", "Ваша заявка успешно отправлена!")

root = tk.Tk()
root.title("Форма заявки на работу в зоопарке")
root.geometry("500x600")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))

contact_frame = ttk.LabelFrame(root, text="Контактная информация", padding=10)
contact_frame.pack(pady=10, padx=10, fill="x")

ttk.Label(contact_frame, text="Имя *").grid(row=0, column=0, sticky="w")
name_entry = ttk.Entry(contact_frame)
name_entry.grid(row=0, column=1, sticky="ew", pady=5)

ttk.Label(contact_frame, text="Телефон").grid(row=1, column=0, sticky="w")
phone_entry = ttk.Entry(contact_frame)
phone_entry.grid(row=1, column=1, sticky="ew", pady=5)

ttk.Label(contact_frame, text="Email *").grid(row=2, column=0, sticky="w")
email_entry = ttk.Entry(contact_frame)
email_entry.grid(row=2, column=1, sticky="ew", pady=5)

personal_frame = ttk.LabelFrame(root, text="Персональная информация", padding=10)
personal_frame.pack(pady=10, padx=10, fill="x")

ttk.Label(personal_frame, text="Возраст *").grid(row=0, column=0, sticky="w")
age_entry = ttk.Entry(personal_frame)
age_entry.grid(row=0, column=1, sticky="ew", pady=5)

ttk.Label(personal_frame, text="Пол").grid(row=1, column=0, sticky="w")
gender_var = tk.StringVar()
ttk.Radiobutton(personal_frame, text="Мужчина", variable=gender_var, value="Мужчина").grid(row=1, column=1, sticky="w")
ttk.Radiobutton(personal_frame, text="Женщина", variable=gender_var, value="Женщина").grid(row=2, column=1, sticky="w")

ttk.Label(personal_frame, text="Личные качества").grid(row=3, column=0, sticky="nw")
qualities_entry = tk.Text(personal_frame, height=4, width=30)
qualities_entry.grid(row=3, column=1, sticky="ew", pady=5)

animals_frame = ttk.LabelFrame(root, text="Выберите ваших любимых животных", padding=10)
animals_frame.pack(pady=10, padx=10, fill="x")

animals = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]
animals_vars = {}

for i, animal in enumerate(animals):
    animals_vars[animal] = tk.BooleanVar()
    cb = ttk.Checkbutton(animals_frame, text=f"💬 {animal}", variable=animals_vars[animal])
    cb.grid(row=i//2, column=i%2, sticky="w", padx=5, pady=2)

submit_btn = ttk.Button(root, text="Отправить информацию", command=submit_form)
submit_btn.pack(pady=20)

root.mainloop()
