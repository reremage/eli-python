def sum(a, b):
    return(a + b)
def prod(a, b):
    return(a * b)

for i in range(0, 10):
    if (i <= 1):
        print(f'Current Number {i} Previous Number {i} Sum: {i + i}')
    else:
        print(f'Current Number {i} Previous Number {i-1} Sum: {i + (i - 1)}')
