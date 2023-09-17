#!/usr/bin/env python
#basic_functions.py
def multiply(x,y):
    return x * y

def hello_name(x='you'):
    return (f'Hello, {x}!')

def less_than_ten(x):
    z = []
    for y in x:
        if y < 10:
            z.append(y)
    return z

print(multiply(10,5))
print(hello_name())
print(less_than_ten([1, 5, 81, 10, 8, 2, 102]))