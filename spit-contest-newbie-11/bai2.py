import math

n, x = map(int, input().split())
tuSo = n + 5 * 10**(x - 1);
mauSo = 10**x
rs = math.floor(tuSo/mauSo) * 10**x
print(rs)

