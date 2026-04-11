def sum(a, b):
    return (a + b)
def mod(a, b):
    return (a % b)
def prod(a, b):
    return (a * b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

print(f'Product of {a} and {b} is {prod(a, b)}')

print(f'Remainder of {a} and {b} is {mod(a, b)}')

if (a % 2 == 0):
    print(f'{a} is even')
else:
    print(f'{a} is odd')
    
if (b % 2 == 0):
    print(f'{b} is even')
else:
    print(f'{b} is odd')
