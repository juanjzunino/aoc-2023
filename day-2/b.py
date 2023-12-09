from collections import defaultdict


def main() -> None:
    with open('./input.txt', 'r') as f:
        powers = 0
        for line in f.readlines():
            _, subsets = line.split(': ')
            subsets_list = list(map(lambda x: x.strip().split(', '), subsets.split('; ')))
            d = defaultdict(int)
            for subset in subsets_list:
                for package in subset:
                    load, color = package.split(' ')
                    if int(load) > d[color]:
                        d[color] = int(load)
            power = 1
            for color, load in d.items():
                power *= load
            powers += power
        print(powers)


if __name__ == '__main__':
    main()
