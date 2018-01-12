daemi = raw_input()

n = int(raw_input())

maxStig = 0

for i in range(n):
    asd = raw_input().split()
    if asd[1] == daemi:
        maxStig = max(maxStig, int(asd[2]))

print maxStig
