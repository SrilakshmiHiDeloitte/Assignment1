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
