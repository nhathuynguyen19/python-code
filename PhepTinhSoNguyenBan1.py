
def main():
    a, b = map(int, input().split())
    rs = [0] * 5
    rs[0] = a + b
    rs[1] = a - b
    rs[2] = a * b
    rs[3] = a // b
    rs[4] = a % b

    print(f"{a} + {b} = {rs[0]}")
    print(f"{a} - {b} = {rs[1]}")
    print(f"{a} * {b} = {rs[2]}")
    print(f"{a} / {b} = {rs[3]}")
    print(f"{a} % {b} = {rs[4]}")

if __name__ == "__main__":
    main()