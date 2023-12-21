def main() -> None:
    originals = []
    copies = []
    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            scratchcard, cards = line.split(': ')
            scratchcard_id = int(scratchcard.split(' ')[-1])
            winning_str, stack_str = cards.split(' | ')
            winning = set(map(int, winning_str.split()))
            stack = set(map(int, stack_str.split()))
            matches_len = len(stack.intersection(winning))
            originals.append(scratchcard_id)
            copies_won = list(range(scratchcard_id + 1, scratchcard_id + matches_len + 1))
            copies.extend(copies_won)
            occurrences = copies.count(scratchcard_id)
            for _ in range(occurrences):
                copies.extend(copies_won)
        copies.extend(originals)
        print(len(copies))


if __name__ == '__main__':
    main()
