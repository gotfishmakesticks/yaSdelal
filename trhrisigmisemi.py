import tkinter as tk

root = tk.Tk()
root.geometry("800x450")
root.resizable(height=False, width=False)

field_1 = tk.Frame()
field_1.grid(row=0, column=0, padx=10, pady=20)

field_2 = tk.Frame()
field_2.grid(row=0, column=1, padx=10, pady=20)

for i in range(10):
    for j in range(10):
        tk.Button(field_1, height=2, width=4).grid(row=i, column=j)
for i in range(10):
    for j in range(10):
        tk.Button(field_2, height=2, width=4).grid(row=i, column=j)

root.mainloop()
