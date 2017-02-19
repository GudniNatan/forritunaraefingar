s = raw_input()
finalString = list()
for i in range(len(s)):
    if s[i] == '<' and len(finalString) > 0:
        finalString.pop()
    elif s[i] != '<':
        finalString.append(s[i])
str1 = ''.join(finalString)
print str1