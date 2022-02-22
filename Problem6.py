# Problem 1
def multiply(func):
    def mult(num1, num2):
        print(num1 * num2)
        func(num1, num2)

    return mult


@multiply
def final(num1, num2):
    print(num1 * num2)


final(2, 3)


# Problem2

def my_range(n):
    first = 0
    second = 1
    third = first + second
    print(first)
    print(second)

    while third <= n:
        yield third
        first = second
        second = third
        third = first + second


for i in my_range(20):
    print(i)
