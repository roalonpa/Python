import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Functions

def create_widget(widget, parent, **options):
    return widget(parent, **options)

keys = []
expression = []
ops = [('AC', 7, 4, 1, '√'), ('DEL', 8, 5, 2, 0), ('.', 9, 6, 3, '^'), ('+', '-', '*', '/', '=')]    

def on_op(op):
    if op == 'AC':
        keys.clear()
    elif op == '=':
        result()
    elif op == 'DEL':
        if keys:
            keys.remove(keys[-1])
    elif op == '':
        pass
    elif op == '^':
        keys.append('**')
    elif op == '√':
        keys.append('**0.5')
    else:
        keys.append(op)
    print(keys)
    screen.config(text=keys)

def create_expression():
    num = ''
    for item in keys:
        if isinstance(item, int) or (isinstance(item, str) and item == '.'):
            num += str(item)
        else:
            if num:
                expression.append(num)
                num = ''
            expression.append(str(item))
    if num:
        expression.append(num)
    return " ".join(expression)

def result():
    expr = create_expression()
    try:
        result_value = round(eval(expr), 5)
        keys.clear()
        keys.extend([int(x) if x.isdigit() else x for x in str(result_value)])
        expression.clear()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {expr}")
        keys.clear()
        expression.clear()
        screen.config(text="")
    


# Interface
window = create_widget(tk.Tk, None)
window.title('Calculator')
window.geometry('350x500')

frame_main = create_widget(ttk.Frame, window, style='Main.TFrame')
frame_main.pack(expand=True, fill='both')

screen = create_widget(ttk.Label, frame_main, text="", style='Screen.TLabel')
screen.pack(fill='y', expand=True)

frame_operations = create_widget(ttk.Frame, frame_main, style='Main.TFrame')
frame_operations.pack(expand=True, fill='both')

for col in ops:
    for op in col:
        if op == '=' or op == '+' or op == '-' or op == '*' or op == '/':
            style = 'Operator.TButton'
        elif op == 'AC' or op == 'DEL' or op == '':
            style = 'Control.TButton'
        else:
            style = 'Number.TButton'
        btn = create_widget(
            ttk.Button, 
            frame_operations, 
            text=op, 
            width=2,
            command = lambda op=op: on_op(op),
            style=style
            )
        btn.grid(
            row = col.index(op), 
            column = ops.index(col),
            padx=2,
            pady=2,
            sticky="nsew"
        )

for i in range(len(ops[0])):  # Number of rows
    frame_operations.rowconfigure(i, weight=1)
for j in range(len(ops)):     # Number of columns
    frame_operations.columnconfigure(j, weight=1)



# Styles

style = ttk.Style()
style.theme_use('clam')

main_frames_style = ttk.Style()
main_frames_style.configure('Main.TFrame',
                            borderwidth = 0,
                            padding = 5,
                            background = "#F6F6F6"
                            )

screen_style = ttk.Style()
screen_style.configure('Screen.TLabel',
                       font=('Arial', 24, 'bold'),
                       padding=10,
                       background="#F6F6F6",
                       )

btn_style = ttk.Style()
btn_style.configure('TButton',
                    font=('Arial', 20),
                    padding=10,
                    borderwidth=2,
                    relief='sunken',
                   )

operator_btn_style = ttk.Style().configure('Operator.TButton',
                    background="#F8FFED",
                   )

control_btn_style = ttk.Style().configure('Control.TButton',
                    background="#DEDEDE",
                   )

number_btn_style = ttk.Style().configure('Number.TButton',
                    background="#EEEEEE",
                   )


window.mainloop()