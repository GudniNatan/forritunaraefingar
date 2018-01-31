import math
n = int(raw_input())

x = str(oct(n))[1::]
xOG = x
for i in range(len(x)-1, -1, -1):
    if x[i]== '0':
        x = str(int(int(x) - math.pow(10, (len(x) - i - 1))))
    elif x[i] == '9' and xOG[i] == '0':
        x = str(int(int(x) - math.pow(10, (len(x) - i - 1)) * 2))

print x
