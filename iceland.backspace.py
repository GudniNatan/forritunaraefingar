line = list()
for char in input():
    if char == "<":
        line.pop()
    else:
        line.append(char)
print("".join(line))
