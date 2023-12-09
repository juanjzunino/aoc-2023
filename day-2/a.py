def main() -> None:
    limits = {'red': 12, 'green': 13, 'blue': 14}
    with open('./input.txt', 'r') as f:
        ids = []
        for line in f.readlines():
            game, subsets = line.split(': ')
            subsets_list = list(map(lambda x: x.strip().split(', '), subsets.split('; ')))
            feasible = []
            for subset in subsets_list:
                for package in subset:
                    load, color = package.split(' ')
                    if int(load) > limits[color]:
                        feasible.append(False)
                    else:
                        feasible.append(True)
            if all(feasible):
                _, _id = game.split(' ')
                ids.append(int(_id))
        print(sum(ids))


if __name__ == '__main__':
    main()
