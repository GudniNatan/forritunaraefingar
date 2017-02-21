numbers = map(int, raw_input().split())
numbers.sort()
abc = raw_input()
string = ""
for i in range(len(abc)):
    if abc[i] == "A":
        print(numbers[0]),
    if abc[i] == "B":
        print(numbers[1]),
    if abc[i] == "C":
        print(numbers[2]),

