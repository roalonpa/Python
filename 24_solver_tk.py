from itertools import permutations
from itertools import product
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def create_widget(widget, parent, **opt): # Create a widget with a parent and options
    return widget(parent, **opt)

def create_entry(parent): # Create an entry widget with validation for numbers
    entry = create_widget(tk.Entry, parent)

    def validate_number(num):
        return num == '' or num.isdigit()
    vcmd = (window.register(validate_number), '%P')
    entry.config(validate='key', validatecommand=vcmd)

    entry.config(width=10, font=('Open Sans', 16, 'bold'), justify='center')
    entry.pack_configure(ipady=5)
    entry.pack(side='left', expand=True)
    return entry

#interface
window = create_widget(tk.Tk, None)
window.title('Solver')
window.geometry('600x300')
window.configure(background='lightblue')

#Title
title = create_widget(tk.Label, window, text="Enter four numbers to find all possible operations that result in 24", bg='lightblue')
title.config(font=('Open Sans', 12, 'bold'))
title.pack_propagate(False)
title.pack(pady=10)

# entries
frame_entries = create_widget(tk.Frame, window)
frame_entries.config(width=500, height=80, bd=2, bg='lightblue')
frame_entries.pack(pady=0)
frame_entries.pack_propagate(False)

#create the entry from the function
entry_num1 = create_entry(frame_entries)
entry_num2 = create_entry(frame_entries)
entry_num3 = create_entry(frame_entries)
entry_num4 = create_entry(frame_entries)

#Create a frame for the operation
frame_operation = create_widget(tk.Frame, window)
frame_operation.config(bd=0, width=500, height=160, bg='lightblue')
frame_operation.pack()
frame_operation.pack_propagate(False)

#Create an inner frame for the operation
frame_operation_inner = create_widget(tk.Frame, frame_operation)
frame_operation_inner.pack(expand=True)


def on_solve(): # Handle the operation when button is pressed
    if not entry_num1.get() or not entry_num2.get() or not entry_num3.get() or not entry_num4.get():
        messagebox.showwarning("Input Error", "Please enter all numbers.")
        return

    a = int(entry_num1.get())
    b = int(entry_num2.get())
    c = int(entry_num3.get())
    d = int(entry_num4.get())
    # Clear entries after reading values
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_num3.delete(0, tk.END)
    entry_num4.delete(0, tk.END)
    #variables

    game = [a, b, c, d]
    operations = ['+', '-', '*', '/']
    expressions = [] #list to hold all expressions
    results = {} #dictionary to hold expression results

    #all possible combinations
    game_permutations = list(permutations(game)) #all possible orders of the numbers
    operations_permutations = list(product(operations, repeat=3)) #all possible combinations of operations

    for game_perms in game_permutations: #create expressions
        for op_perms in operations_permutations: #for each combination of operations and order of numbers
            exp = (game_perms[0], op_perms[0], game_perms[1], op_perms[1], game_perms[2], op_perms[2], game_perms[3])
            expressions.append(exp) #append expression to list


    parentesis = [] #tuple to hold expressions with parentheses
    def add_parentesis(op, expr): #function to add parentheses around an operation
        if op in expr:
            expr_list = list(expr)
            index = expr_list.index(op)
            expr_list.insert((index - 1), '(')
            index = expr_list.index(op)
            expr_list.insert((index + 2), ')')
            expr = tuple(expr_list)
            parentesis.append(expr)
    for expr in expressions: #add parentheses to expressions
     add_parentesis('+', expr)
     add_parentesis('-', expr)
     if (expr[1] == '+' and expr[5] == '-') or (expr[1] == '-' and expr[5] == '+'):
         exp_list = list(expr)
         exp_list.insert(0, '(')
         exp_list.insert(4, ')')
         exp_list.insert(6, '(')
         exp_list.insert(10, ')')
         exp = tuple(exp_list)
         parentesis.append(exp)
    expressions.extend(parentesis) #add expressions with parentheses to main list

    for expr in expressions: #convert into / evaluate expressions
     expr_str = "".join(str(i) for i in expr) #create string from tuple
     try:
         result = eval(expr_str) #evaluate expression
     except ZeroDivisionError: #ignore division by zero errors
         continue
     results[expr_str] = result #store expression and result in dictionary

    for expr, res in results.items(): #print results = 24
     if res == 24:
         print(f"{expr} = {round(res)}")
    found = False
    result_str = ""
    for expr, res in results.items(): #print results = 24
        if res == 24:
            result_str += f"{expr} = {round(res)}\n"
            found = True
    if found:
        messagebox.showwarning(
            title="Result",
            message= result_str , 
            icon="warning")
    else:
        messagebox.showinfo("Results", "No solution found that equals 24.")

#Create the button
btn_frame = create_widget(tk.Frame, frame_operation_inner)
btn_frame.config(width=800, height=1000, bd=2)
btn = create_widget(tk.Button, btn_frame, text="Solve", command=on_solve)
btn.config(font=('Open Sans', 40), borderwidth=0, highlightthickness=0, bg="white", fg="black", activebackground="lightgrey")
btn_frame.pack(side='left')
btn_frame.pack_propagate(False)
btn.pack(expand=True, fill='both')

window.mainloop()