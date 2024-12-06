from tkinter import *
tk = Tk()
# квадратный массив кнопок с индивидуальными командами
b = [[ Button(tk, command=lambda: send(0, 0, back)),
       Button(tk, command=lambda: send(0, 1, back)),
       Button(tk, command=lambda: send(0, 2, back))],
     [ Button(tk, command=lambda: send(1, 0, back)),
       Button(tk, command=lambda: send(1, 1, back)),
       Button(tk, command=lambda: send(1, 2, back))],
     [ Button(tk, command=lambda: send(2, 0, back)),
       Button(tk, command=lambda: send(2, 1, back)),
       Button(tk, command=lambda: send(2, 2, back))],]

# настройка внешнего вида кнопок
for r in range(3):
    for c in range(3):
        b[r][c].config(font="Consolas 44", width=4, text=" ")
        b[r][c].grid(row=r, column=c)

# функция обратного вызова - ставит значки на кнопках, сообщает о победе
def back(r, c, what, winner):
    global b
    if winner != 2:
        tk.title("Победил " + ("нолик", "крестик")[winner])
        disableButtons()
    b[r][c]["text"] = "0X"[what]

def disableButtons():
    for r in range(3):
        for c in range(3):
            b[r][c]["command"] = ''

# Модель в виде числовой таблицы с числами: 0-нолик, 1-крестик, 2-пусто
S = 2
X = 1
field = [ [S,S,S], [S,S,S], [S,S,S], ]

# Что ставить на очередном ходе - крестик или нолик
# Начинаем с крестика
current = X

# Команда, которую модуль main подает модели
def send(r, c, back):
    global current, field
    if field[r][c] == S:
        field[r][c] = current
        current = (current + 1) % 2
        back(r, c, field[r][c], getWinner(field))

def getWinner(m):
    # по гризонтали
    if m[0][0] == m[0][1] == m[0][2] != S: return m[0][0]
    if m[1][0] == m[1][1] == m[1][2] != S: return m[1][0]
    if m[2][0] == m[2][1] == m[2][2] != S: return m[2][0]
    # по вертикали
    if m[0][0] == m[1][0] == m[2][0] != S: return m[0][0]
    if m[0][1] == m[1][1] == m[2][1] != S: return m[0][1]
    if m[0][2] == m[1][2] == m[2][2] != S: return m[0][2]
    # по диагонали
    if m[0][0] == m[1][1] == m[2][2] != S: return m[0][0]
    if m[2][0] == m[1][1] == m[0][2] != S: return m[2][0]
    return 2

tk.mainloop()
