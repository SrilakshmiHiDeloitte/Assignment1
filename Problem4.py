
# Problem1
import cmath

x = lambda a, b, c: ((-b - cmath.sqrt(b ** 2 - (4 * a * c))) / (2 * a), (-b + cmath.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
print(x(2, 4, 1))


# Problem2
a = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
x = sum(list(map(lambda b: (i for i in a if 'A' in i or 'a' in i), a)))

print(x)
