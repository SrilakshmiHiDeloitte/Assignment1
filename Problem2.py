def pattern1(n):
    """j = 1
    for i in range(0, n):
        k = i + j
        print(k*"*")
        j = j + 1"""
    m = 1
    for i in range(0, n):
        k = ((n-i)*'  ')
        l = (i+m)*'*'
        m = m+1

        print(k,l)
    m = n-1
    for i in reversed(range(0, n-1)):
        k = ((n - i) * '  ')
        l = (i + m) * '*'
        m = m - 1

        print(k, l)

        """for k in range(0, i + 2):
            print("*", end="")"""

def pattern2(n):
    for i in range(n):
        # printing spaces
        for j in range(n - i - 1):
            print(' ', end='')

        # printing stars
        for k in range(2 * i + 1):
            # print star at start and end of the row
            if k == 0 or k == 2 * i:
                print('*', end='')
            else:
                if i == n - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
        print(end='\n')


pattern1(5)
