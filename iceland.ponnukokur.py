n, q = list(map(int, input().split()))

kokur = [0 for _ in range(n)]
count1 = 0
flip = False
segments = [0 for __ in range(1001)]
for i in range(q):
    a = list(map(int, input().split()))

    if a[0] == 1:
        a[1] -= 1
        kokur[a[1]] = 1 if kokur[a[1]] == 0 else 0
        count1 += 1 if kokur[a[1]] == 1 else -1
        segments[a[1] // 100] += 1 if kokur[a[1]] == 1 else -1
    if a[0] == 2:
        flip = not flip
    if a[0] == 3:
        if not flip:
            print(count1)
        else:
            print(n - count1)
    if a[0] == 4:
        count2 = 0
        a[1] -= 1
        temp = 0
        if a[2] - a[1] < 250:
            temp = sum(kokur[a[1]:a[2]])
        else:
            tracker = a[1]
            while tracker % 100 != 0:
                temp += kokur[tracker]
                tracker += 1
            while tracker + 100 < a[2]:
                temp += segments[tracker // 100]
                tracker += 100
            while tracker <= a[2]:
                temp += kokur[tracker]
                tracker += 1

        if flip:
            temp = a[2] - a[1] - temp
        print(temp)