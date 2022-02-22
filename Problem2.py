def pattern1(n):
    m = 1
    for i in range(0, n):
        k = ((n - i) * '  ')
        l = (i + m) * '*'
        m = m + 1

        print(k, l)
    m = n - 1
    for i in reversed(range(0, n - 1)):
        k = ((n - i) * '  ')
        l = (i + m) * '*'
        m = m - 1

        print(k, l)


def pattern2(n):
    j = 0
    for i in range(1, n + 1):
        if i <= 2 or i == n:
            k = ((n - i) * ' ')
            print(k + i * '* ' + k)
        else:
            k = (n - i) * ' '
            h = (i - 1 + j) * ' '
            print(k + '* ' + h + '* ' + k)
            j = j + 1


def pattern3(n):
    for i in reversed(range(0, n + 1)):
        if i <= 2 or i == n:
            k = (n - i) * '  '
            print(k + (i * '* '))
        else:
            k = (n - i) * '  '
            l = (i - 2) * '  '
            print(k + '* ' + l + '* ')


def pascal(n):
    j = 0
    for i in range(1, n + 1):
        if i <= 2:
            k = (n-i)*' '
            print(k+i*'1 ')
        else:
            k = (n-i) * ' '
            print(k,end='')
            for j in range(1,i):
                print(str(j)+' ',end='')
            print('1 ')





pascal(5)
