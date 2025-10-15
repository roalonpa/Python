import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# functions



def create_widget(widget, parent, **opt): # Create a widget with a parent and options
    return widget(parent, **opt)


def create_entry(parent): # Create an entry widget with validation for numbers
    entry = create_widget(tk.Entry, parent)

    def validate_number(num):
        return num == '' or num == '-' or num.isdigit() or (num.startswith('-') and num[1:].isdigit())
    vcmd = (window.register(validate_number), '%P')
    entry.config(validate='key', validatecommand=vcmd)

    entry.config(width=18, font=('ms serif', 16, 'bold'), justify='center')
    entry.pack_configure(ipady=5)
    entry.pack(side='left', expand=True)
    return entry


def on_enter(operation): # Handle the operation when a button is pressed

    if not entry_num1.get() or not entry_num2.get():
        messagebox.showwarning("Input Error", "Please enter both numbers.")
        return

    num1 = int(entry_num1.get())
    entry_num1.delete(0, tk.END)
    num2 = int(entry_num2.get())
    entry_num2.delete(0, tk.END)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:
        result = round(num1 / num2, 3)

    messagebox.showinfo("result", f"{num1} {operation} {num2} = {result}")

# interface

window = create_widget(tk.Tk, None)

window.title('Calculator')
window.geometry('600x300')

    # entries

frame_entries = create_widget(tk.Frame, window)
frame_entries.config(width=500, height=80, bd=2, relief='sunken')
frame_entries.pack(pady=20)
frame_entries.pack_propagate(False)


entry_num1 = create_entry(frame_entries)

entry_num2 = create_entry(frame_entries)


    # operations

frame_operation = create_widget(tk.Frame, window)
frame_operation.config(bd=2, relief='sunken', width=500, height=160)
frame_operation.pack()
frame_operation.pack_propagate(False)

frame_operation_inner = create_widget(tk.Frame, frame_operation)
frame_operation_inner.pack(expand=True)

for op in ['+', '-', '*', '/']:
    btn_frame = create_widget(tk.Frame, frame_operation_inner)
    btn = create_widget(tk.Button, btn_frame, text=op, command=lambda op=op: on_enter(op))

    btn_frame.config(width=60, height=60, bd=2, relief='sunken')
    btn.config(font=('courier new', 28), borderwidth=0, highlightthickness=0, relief='flat')

    btn_frame.pack(side='left', padx=5)
    btn_frame.pack_propagate(False)
    btn.pack(expand=True, fill='both')


window.mainloop()