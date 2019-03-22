n, k = list(map(int, input().split()))

if (n - 1) % (k + 1) < k or k >= n :
    print("Jebb")
else:
    print("Neibb")