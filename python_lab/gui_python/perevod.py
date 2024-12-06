import tkinter as tk
def convert():
    num = int(entry_num.get())
    result = ""
    chars = "0123456789"
    while num > 0:
        result = chars[num % 2] + result
        num //= 2
    lbl_result.config(text=f"Результат: {result}", fg="black")

root = tk.Tk()
root.title("Перевод в систему счисления")
root.geometry("400x400")

# Поле для ввода числа
tk.Label(root, text="Введите число:").place(x=20, y=20)
entry_num = tk.Entry(root, width=20)
entry_num.place(x=150, y=20)

btn_convert = tk.Button(root, text="Конвертировать", command=convert)
btn_convert.place(x=20, y=100)

lbl_result = tk.Label(root, text="")
lbl_result.place(x=20, y=140)

root.mainloop()

