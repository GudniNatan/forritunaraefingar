t = int(raw_input())

cases = {
    "c": [1, 2, 3, 6, 7, 8, 9],
    "d": [1, 2, 3, 6, 7, 8],
    "e": [1, 2, 3, 6, 7],
    "f": [1, 2, 3, 6],
    "g": [1, 2, 3],
    "a": [1, 2],
    "b": [1],
    "C": [2],
    "D": [0, 1, 2, 3, 6, 7, 8],
    "E": [0, 1, 2, 3, 6, 7],
    "F": [0, 1, 2, 3, 6],
    "G": [0, 1, 2, 3],
    "A": [0, 1, 2],
    "B": [0, 1]
}

for case in xrange(t):
    hits = [0 for x in range(10)]
    buttons = [False for x in range(10)]
    song = raw_input()
    for c in song:
        b = cases[c]
        for i in range(10):
            if i in b:
                if not buttons[i]:
                    buttons[i] = True
                    hits[i] += 1
            else:
                buttons[i] = False
    print " ".join(map(str, hits))
