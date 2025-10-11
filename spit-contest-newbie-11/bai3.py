import math

x, y, k = map(int, input().split())

if x >= y:
    print(0)
else:
    n = math.ceil((y - x) / k)
    T = 0
    for i in range(n - 1):
        T += 2 * (x + (i + 1) * k)
    T += y
    print(T)
