def main() -> None:
    with open('./input.txt', 'r') as f:
        points = 0
        for line in f.readlines():
            _, cards = line.split(': ')
            winning_str, stack_str = cards.split(' | ')
            winning = set(map(int, winning_str.split()))
            stack = set(map(int, stack_str.split()))
            matches = stack.intersection(winning)
            point = 2 ** (len(matches) - 1) if len(matches) > 0 else 0
            points += point
        print(points)


if __name__ == '__main__':
    main()
