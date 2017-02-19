import math
#Ekki full lausn

def dist((x1, y1), (x2, y2)):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def total_distance(points):
    return sum([dist(point, points[index + 1]) for index, point in enumerate(points[:-1])])

def travelling_salesman(points, start=(0, 0)):
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: dist(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    path.append(start)
    return path

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
    print total_distance(travelling_salesman(packages))

main()