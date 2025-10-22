import tkinter as tk
from tkinter import messagebox

def largest_even(list):
    even = []
    for num in list:
        if num % 2 == 0:
            even.append(num)
    if even == []:
        messagebox.showinfo("no even", "There are no even numbers")
    else:
        messagebox.showinfo("largest even", max(even))

def on_enter():
    num1 = int(e1.get())
    e1.delete(0, tk.END)
    num2 = int(e2.get())
    e2.delete(0, tk.END)
    num3 = int(e3.get())
    e3.delete(0, tk.END)
    num4 = int(e4.get())
    e4.delete(0, tk.END)
    num5 = int(e5.get())
    e5.delete(0, tk.END)
    list = [num1, num2, num3, num4, num5]
    largest_even(list)



window = tk.Tk()
window.title("Find Largest Even Number")
window.geometry("600x400")

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Entry(window)
e5 = tk.Entry(window)

# When a lot of entries have to be made, they can not be done with a for, because a for loop would define all 5 entries with the same name, which would be ok if that values had to be used in that same moment, but as we are using tk, and there will be a visual interface, those entries have to be always shown on screen, but their values cannot be used until each of them is filled and the button is pressed, so each one of them must have its own separate identity. Tk is different from a common python code, because in a common loop, the loop defines a variable for the input and adds that value to a list, so the next input is called with the same variable, which cannot be done with Tkinter

e1.pack()
e2.pack()
e3.pack()
e4.pack()
e5.pack()

btn = tk.Button(window, text="Find", command=lambda:on_enter())
btn.pack()

window.mainloop()
