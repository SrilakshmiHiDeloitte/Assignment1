# Problem1
import cmath

x = lambda a, b, c: (
(-b - cmath.sqrt(b ** 2 - (4 * a * c))) / (2 * a), (-b + cmath.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
print(x(2, 4, 1))

# Problem2
a = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

op = []
y = sum(list(map(lambda x: (x.count('A')) if 'A' in x or 'a' in x else x, a)))
z = sum(list(map(lambda x: (x.count('a')) if 'a' in x else a, a)))
op.append(y)
op.append(z)
print(op)
