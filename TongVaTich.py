def main():

    m, n = map(int, input().split())

    print(f"{(m % 10) + (n % 10)}")
    print(f"{(m // 1000) * (n // 1000)}")


if __name__ == "__main__":
    main()