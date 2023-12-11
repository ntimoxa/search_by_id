import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def search_employee():
    try:
        search_id = int(entry.get())
        df = pd.read_excel('2_task.xlsx', sheet_name='вариант 1')
        result_df = df[df['ИД'] == search_id]

        if not result_df.empty:
            top = tk.Toplevel(root)
            top.title("Информация по сотруднику")

            # Создание функции для выхода из полноэкранного режима
            def exit_fullscreen(event=None):
                top.attributes("-fullscreen", False)
                top.unbind("<Escape>")
                top.bind("<F11>", toggle_fullscreen)

            # Создание функции для переключения в полноэкранный режим
            def toggle_fullscreen(event=None):
                top.attributes("-fullscreen", True)
                top.bind("<Escape>", exit_fullscreen)
                top.unbind("<F11>")

            toggle_fullscreen()  # Вход в полноэкранный режим

            label = tk.Label(top, text="Информация по сотруднику:", font=('Arial', 24, 'bold'))
            label.pack()

            # Создание таблицы с данными
            tree = ttk.Treeview(top, show="headings")  # Изменение настроек, чтобы скрыть первую колонку
            tree["columns"] = list(result_df.columns)
            for col in result_df.columns:
                tree.heading(col, text=col)
                tree.column(col, width=150,
                            anchor='center')  # Установка ширины столбцов и выравнивание данных по центру
            for index, row in result_df.iterrows():
                tree.insert("", tk.END, values=list(row))
            tree.pack(fill=tk.BOTH, expand=True)

            # Создание кнопки для выхода из полноэкранного режима
            exit_button = tk.Button(top, text="Выйти из полноэкранного режима", command=exit_fullscreen)
            exit_button.pack()

        else:
            messagebox.showerror("Ошибка", "Сотрудник с указанным ИД не найден")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целочисленное значение ИД")


root = tk.Tk()
root.title("Поиск информации о сотруднике")

label = tk.Label(root, text="Введите ИД сотрудника:", font=('Arial', 24))
label.pack()

entry = tk.Entry(root, font=('Arial', 24), width=20)
entry.pack(pady=10)

button = tk.Button(root, text="Найти", command=search_employee, font=('Arial', 24))
button.pack(pady=10)

# Выравнивание элементов по центру окна
root.update_idletasks()
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()
