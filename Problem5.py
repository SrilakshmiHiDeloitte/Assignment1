# Problem3
a = [-1000, 500, -600, 700, 5000, -90000, -17500]


def positive(n):
    if n < 0:
        n = -n
    return n


x = list(map(positive, filter(positive, a)))
print(x)

# Problem 4



# Problem 5
def keyval(a, b):
    c = {i: j for i, j in zip(a, b)}
    print(c)


keyval(["Netflix", "Hulu", "Sling", "Hbo"], [198, 166, 237, 125])
