import array as arr


def duplicate(n):
    c = 0
    op = {}
    for i in n:
        for k in i:
            c = 0
            for m in i:
                if k == m:
                    c = c + 1
            if c >= 2:
                op[k] = c
    print(op)


duplicate([[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]])


def merge(a, b):
    output = []
    for i in a:
        op = ''
        for j in b:
            op = str(i) + str(j)
            output.append(op)
    print(output)


merge(["Hello ", "take "], ["Dear", "Sir"])


def appendlist(a, b):
    c = a[2][1][2]
    for i in b:
        c.append(i)
    print(a)


appendlist(["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"], ['h', 'i', 'j'])


def mapping(a, b):
    c = {i: j for i, j in zip(a, b)}
    print(c)


mapping(['Ten', 'Twenty', 'Thirty'], [10, 20, 30])


def replacing(a, b):
    for i in a.keys():
        if i == 'city':
            a[i] = b
    print(a)


replacing({"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}, 'Rajahmundry')


def dictolist(a):
    op = []
    for i in a.keys():
        m = a.get(i)
        m.insert(0,i)
        op.append(m)
    print(op)


dictolist({'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]})
