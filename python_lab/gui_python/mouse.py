import tkinter as tk

class Drag(tk.Label):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)
        self.drag_data = {"x": 0, "y": 0}

    def on_press(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag(self, event):
        # Расчет смещения
        delta_x = event.x - self.drag_data["x"]
        delta_y = event.y - self.drag_data["y"]
       
        new_x = self.winfo_x() + delta_x
        new_y = self.winfo_y() + delta_y

       
        max_width = self.master.winfo_width() - self.winfo_width()
        max_height = self.master.winfo_height() - self.winfo_height()

        new_x = max(0, min(new_x, max_width))
        new_y = max(0, min(new_y, max_height))

       
        self.place(x=new_x, y=new_y)

    def on_release(self, event):
        self.drag_data["x"] = 0
        self.drag_data["y"] = 0


root = tk.Tk()
root.geometry("500x500")

label = Drag(root, text="Тащи меня", font=("Arial", 14), bg="lightblue", padx=10, pady=5)
label.place(x=100, y=100)

root.mainloop()
