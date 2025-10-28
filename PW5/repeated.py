def first_repeated_digit(n):
    not_repeated = []
    for digit in str(n):
        if digit in not_repeated:
            return f'the first repeated digit in {n} is {digit}'
        else:
            not_repeated.append(digit)
    return f'there are no repeated digits in {n}'


n = int(input("enter a number: "))
print(first_repeated_digit(1234567890))
print(first_repeated_digit(112345))
print(first_repeated_digit(n))