n = int(input())
soLinhThach = 0
linhThachNhatPham = 0
linhThachNhiPham = 0
linhThachNguPham = 0
while True:
    if n >= 5:
        linhThachNguPham += 1
        n -= 5
    elif n >= 2:
        linhThachNhiPham += 1
        n -= 2
    elif n >= 1:
        linhThachNhatPham += 1
        n -= 1
    else:
        break
soLinhThach = linhThachNguPham + linhThachNhatPham + linhThachNhiPham
print(soLinhThach) 