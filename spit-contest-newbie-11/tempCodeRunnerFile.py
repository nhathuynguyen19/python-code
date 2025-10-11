import time

x, y ,k = map(int, input().split())

thoi_gian_tong = 0    
robot = 0
hang = x
pin = k
cho_hang = True

while True:
    if pin > 0:
        robot += 1
    # print(f"vi tri robot: {robot}, vi tri hang: {hang}, pin: {pin}")
    thoi_gian_tong += 1
    if hang == robot and pin > 0:
        hang += 1
        robot += 2
        pin -= 1
    
    if pin <= 0:
        robot -= 1
        if robot == 0:
            robot -= 1
            pin = k

    if hang >= y:
        thoi_gian_tong += 1
        break

    # time.sleep(1)

print(thoi_gian_tong)
