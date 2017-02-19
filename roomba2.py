def main():
    size = raw_input().split()
    size = [int(size[0]), int(size[1])]
    lengd = size[0] * size[1]
    if min(size) == 1:
        lengd *= 2
        lengd -= 2
    elif size[0] % 2 == 1 and size[1] % 2 == 1:
        lengd += 1

    x = 0
    y = 0
    lastmove = [0, 0]
    finishing = False
    print "0 0"
    if size[0] == 1 and size[1] == 1:
        return
    if size[0] == 1 or size[1] == 1:
        for i in range(1, max(size)):
            if size[1] > size[0]:
                print "0 "+ str(i)
            else:
                print str(i) + " 0"
        for i in range(max(size) - 1, 1, -1):
            if size[1] > size[0]:
                print "0 "+ str(i - 1)
            else:
                print str(i - 1) + " 0"
        print "0 0"
        return
    for i in range(lengd):
        move = [0, 0]
        if not finishing:
            if x == 0:
                if y == size[1] - 1:
                    move[0] = 1
                else:
                    move[1] = 1
            elif y == size[1] - 1:
                if x == size[0] - 1:
                    move[1] = -1
                else:
                    move[0] = 1
            elif size[1] == 2:
                if x == 1:
                    print "0 0"
                    return
                else:
                    move[0] = -1
            elif x == 2 and y == size[1] - 2:
                move[0] = -1
                finishing = True
            elif (size[0] - (x + 1)) % 2 == 0:
                if y == 0:
                    move[0] = -1
                else:
                    move[1] = -1
            elif y == 0:
                move[1] = 1
            elif y == size[1] - 2:
                move[0] = -1
            else:
                move = lastmove
        else:
            if size[0] % 2 == 1:
                if y == 0 and x == 2:
                    print "1 0"
                    print "0 0"
                    break
                elif lastmove[0] != 0:
                    move[1] = -1
                elif x == 1:
                    move[0] = 1
                else:
                    move[0] = -1
            else:
                if x == 1 and y == 0:
                    print "0 0"
                    return
                else:
                    move[1] = -1

        x += move[0]
        y += move[1]
        lastmove = move
        print str(x) + " " + str(y)

main()