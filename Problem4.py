# Problem1
import cmath

x = lambda a, b, c: (
(-b - cmath.sqrt(b ** 2 - (4 * a * c))) / (2 * a), (-b + cmath.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
print(x(2, 4, 1))

# Problem2
a = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]


y = list(map(lambda x: (a.count(x)) if 'A' in x or 'a' in x else x, a))

print(y)
