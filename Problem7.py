class FormulaError(Exception):
    pass


def calculate(n):
    n = n.split()
    if len(n) != 3:
        raise FormulaError('Input is in wrong format')
    a = n[0]
    b = n[1]
    c = n[2]
    try:
        a = float(a)
        c = float(c)
    except ValueError:
        raise FormulaError('Input is in wrong format')
    return a, b, c


def calculator(a, b, c):
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    raise FormulaError('The math operation is not allowed')


a, b, c = calculate(n='1 - 1')
op = calculator(a, b, c)
print(op)

# Problem 2


a = open('C:\\Users\\visrilakshmi\\Desktop\\test.txt', 'r')
b = []
maximum = 0
c = [line.split(' ') for line in a.readlines()]

for i in c:
    for j in i:
        print(j)
        if len(j) > maximum:
            maximum = len(j)

for i in c:
    if len(i) == maximum:
        print(i)
