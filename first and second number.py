a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

def sum(a, b):
    return(a + b)
def prod(a, b):
    return(a * b)

if (a * b >= 1000):
    print(f'The sum of {a} and {b} is {sum(a, b)}')
else:
    print(f'The product of {a} and {b} is {prod(a, b)}')
    
