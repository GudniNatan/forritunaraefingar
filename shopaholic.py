items = (int(raw_input()), sorted(map(int, raw_input().split())))
print(sum([items[1][i] for i in range(items[0]-3, -1, -3)]))