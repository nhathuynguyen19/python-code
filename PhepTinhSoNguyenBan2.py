def main():
    a, b = map(int, input().split())

    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")

if __name__ == "__main__":
    main()