import tkinter as tk
from tkinter import ttk

class PowersOfTwoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Степени двойки")
        self.root.geometry("400x300")
        
        self.powers = [2**i for i in range(1, 11)]
        
        self.create_widgets()
        self.display_powers()
    
    def create_widgets(self):
  
        title_label = ttk.Label(self.root, text="Степени двойки от 2¹ до 2¹⁰", 
                               font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        list_frame = ttk.Frame(self.root)
        list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        header_frame = ttk.Frame(list_frame)
        header_frame.pack(fill=tk.X)
        
        ttk.Label(header_frame, text="Степень", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        ttk.Label(header_frame, text="Значение", font=("Arial", 10, "bold")).pack(side=tk.RIGHT, padx=5)

        ttk.Separator(list_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        self.text_display = tk.Text(list_frame, height=10, width=40, font=("Courier New", 10))
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.text_display.yview)
        self.text_display.configure(yscrollcommand=scrollbar.set)
        
        self.text_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Показать список", 
                  command=self.display_powers).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Очистить", 
                  command=self.clear_display).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Выход", 
                  command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        self.stats_label = ttk.Label(self.root, text="", font=("Arial", 10))
        self.stats_label.pack(pady=5)
    
    def display_powers(self):
        """Отображает список степеней двойки"""
        self.text_display.delete(1.0, tk.END)
        
        header = f"{'Степень':<10} {'Значение':<15}\n"
        self.text_display.insert(tk.END, header)
        self.text_display.insert(tk.END, "-" * 25 + "\n")
        
        for i, power in enumerate(self.powers, 1):
            line = f"2^{i:<7} {power:<15}\n"
            self.text_display.insert(tk.END, line)
        
        total = sum(self.powers)
        self.stats_label.config(text=f"Всего элементов: {len(self.powers)} | Сумма всех значений: {total}")
    
    def clear_display(self):
        """Очищает поле отображения"""
        self.text_display.delete(1.0, tk.END)
        self.stats_label.config(text="")

def main():
    root = tk.Tk()
    app = PowersOfTwoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
