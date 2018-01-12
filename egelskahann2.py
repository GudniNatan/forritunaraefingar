import math

n = int(raw_input())
a = math.floor(math.log(n, 2))
print int((n - int(math.pow(2, int(a)))) * 2) + 1