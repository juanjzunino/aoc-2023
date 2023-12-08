def main() -> None:
    numbers = []
    with open("./input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            digits = list(filter(lambda x: x.isnumeric(), list(line)))
            numbers.append(int(digits[0] + digits[-1]))
    print(sum(numbers))


if __name__ == "__main__":
    main()
