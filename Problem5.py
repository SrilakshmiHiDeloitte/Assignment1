# Problem3
a = [-1000, 500, -600, 700, 5000, -90000, -17500]


def positive(n):
    if n < 0:
        n = -n
    return n


x = list(map(positive, filter(positive, a)))
print(x)

# Problem 4
from functools import reduce


def red(a, b):
    print(f"a={a}, b={a}, {a} + {b} ={a + b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(red, scores)
print(total)


# Problem 5
def keyval(a, b):
    c = {i: j for i, j in zip(a, b)}
    print(c)


keyval(["Netflix", "Hulu", "Sling", "Hbo"], [198, 166, 237, 125])
