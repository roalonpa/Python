import tkinter as tk
from tkinter import messagebox

def table(n):
    table = []
    for i in range(1, 11):
        res = n*i
        table.append(res)
    messagebox.showinfo("table", table) # to show a message: messagebox.showinfo("title", content)

def on_enter():
    n = int(entry.get()) # to get the value of an entry: if it should be a number add int()
    entry.delete(0, tk.END) # to delete the text of an entry: entry.delete(0, tk.END)
    if n >= 0:
        table(n)
    else:
        messagebox.showinfo("error", "your number must be positive")
        return

window = tk.Tk()

entry = tk.Entry()
entry.pack()

enter = tk.Button (window, command=lambda: on_enter(), text="Enter")
enter.pack()


window.mainloop()