def main() -> None:
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
        digits = [list(filter(lambda x: x.isnumeric(), list(line))) for line in lines]
        print(sum(int(digit[0] + digit[-1]) for digit in digits))


if __name__ == '__main__':
    main()
