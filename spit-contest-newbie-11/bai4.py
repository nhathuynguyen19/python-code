n = int(input())
arr = list(map(int, input().split()))

prev = 0
trend = 0
count = 0

for x in arr:
    if x == 0:
        continue
    if prev == 0:
        prev = x
        continue
    if x > prev:
        if trend == -1:
            count += 1
        trend = 1
    elif x < prev:
        if trend == 1:
            count += 1
        trend = -1
    prev = x

print(count)
