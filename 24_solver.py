from itertools import permutations
from itertools import product

def enter_num(n):
    num = int(input(f"Enter number {n}: "))
    if num >= 1 and num <= 12:
        return num
    else:
        print("Invalid input. Please enter a number between 1 and 12.")
        return enter_num(n)

a = enter_num('one')
b = enter_num('two')
c = enter_num('three')
d = enter_num('four')

game = [a, b, c, d]
operations = ['+', '-', '*', '/']
expressions = []
results = {}

game_permutations = list(permutations(game))
operations_permutations = list(product(operations, repeat=3))

for game_perms in game_permutations:
    for op_perms in operations_permutations:
        exp = (game_perms[0], op_perms[0], game_perms[1], op_perms[1], game_perms[2], op_perms[2], game_perms[3])
        expressions.append(exp)


parentesis = []
def add_parentesis(op, expr):
    if op in expr:
        expr_list = list(expr)
        index = expr_list.index(op)
        expr_list.insert((index - 1), '(')
        index = expr_list.index(op)
        expr_list.insert((index + 2), ')')
        expr = tuple(expr_list)
        parentesis.append(expr)
for expr in expressions:
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
expressions.extend(parentesis)

for expr in expressions:
    expr_str = "".join(str(i) for i in expr)
    try:
        result = eval(expr_str)
    except ZeroDivisionError:
        continue
    results[expr_str] = result

for expr, res in results.items():
    if res == 24:
        print(f"{expr} = {round(res)}")