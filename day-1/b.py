def main() -> None:
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    with open('./input.txt', 'r') as f:
        digits = []
        for line in f.readlines():
            indexes = [(digit, line.index(digit)) for digit in line if digit.isnumeric()]
            indexes.extend([(number, line.index(number)) for number in numbers.keys() if number in line])
            indexes.sort(key=lambda x: x[1])

            first_digit = indexes[0][0]

            if not first_digit.isnumeric():
                first_digit = numbers[first_digit]

            indexes = [(digit, line.rindex(digit)) for digit in line if digit.isnumeric()]
            indexes.extend([(number, line.rindex(number)) for number in numbers.keys() if number in line])
            indexes.sort(key=lambda x: x[1])

            last_digit = indexes[-1][0]

            if not last_digit.isnumeric():
                last_digit = numbers[last_digit]

            digits.append(int(first_digit + last_digit))

        print(sum(digits))


if __name__ == '__main__':
    main()
