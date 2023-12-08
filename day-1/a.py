def main() -> None:
    with open('./input.txt', 'r') as f:
        digits = [list(filter(lambda x: x.isnumeric(), list(line))) for line in f.readlines()]
        print(sum(int(digit[0] + digit[-1]) for digit in digits))


if __name__ == '__main__':
    main()
