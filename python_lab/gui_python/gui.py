import tkinter as tk

def swap():
    text_btn1 = btn1['text']
    text_btn2 = btn2['text']
   
    btn1.config(text=text_btn2)
    btn2.config(text=text_btn1)

root = tk.Tk()
root.title("Превед-Медвед")
root.geometry("400x200")


btn1 = tk.Button(root, text="Медвед-Превед", command=swap)
btn1.place(x=50, y=80)


btn2 = tk.Button(root, text="Превед-Медвед", command=swap)
btn2.place(x=200, y=80)

root.mainloop()
