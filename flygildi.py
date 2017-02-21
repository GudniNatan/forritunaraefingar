import math
import itertools

def dist((x1, y1), (x2, y2)):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def main():
    packageNumber = int(raw_input())
    packages = list()
    minY = 0
    maxY = 0
    packages.append((0, 0))
    Xonly = True
    for i in range(packageNumber):
        coords = raw_input().split()
        packages.append((int(coords[0]),int(coords[1])))
        if int(coords[1]) < minY:
            minY = int(coords[1])
        if int(coords[1]) > maxY:
            maxY = int(coords[1])
        if int(coords[0]) != 0:
            Xonly = False
    if Xonly:
        distance = (maxY - minY) * 2
        print distance
        return
    elif packageNumber == 1:
        print dist(packages[0], packages[1]) * 2
        return
    packages.pop(0)
    minDis = 1000000000
    for route in itertools.permutations(packages):
        route = list(route)
        route.insert(0, (0, 0))
        route.append((0, 0))
        distance = 0
        for i in range(len(route) - 1):
            distance += dist(route[i], route[i+1])
        minDis = min(minDis, distance)

    print minDis

main()