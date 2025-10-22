import tkinter as tk
from tkinter import messagebox

def multiples(n, limit):
    if n <= limit:
        multiples = []
        for num in range(n, limit+1):
            if num % n == 0:
                multiples.append(num)
        messagebox.showinfo("Multiples", multiples)
    else:
        messagebox.showinfo("Error", "Your number cannot be grater than you limit")

def on_enter():
    n = int(e1.get())
    e1.delete(0, tk.END)
    limit = int(e2.get())
    e2.delete(0, tk.END)
    multiples(n, limit)

window = tk.Tk()
window.title("Multiples")
window.geometry("500x200")

frame = tk.Frame(window)
frame.config(width=400, height=100, bd=2, relief="sunken")
frame.propagate(False)
frame.pack()

l1 = tk.Label(frame, text="Insert a number")
l1.pack()

e1 = tk.Entry(frame)
e1.pack()

l2 = tk.Label(frame, text="Insert a limit")
l2.pack()

e2 = tk.Entry(frame)
e2.pack()


btn = tk.Button(window, text="Find Multiples", command=lambda: on_enter())
btn.pack()


window.mainloop()