count = int(input())
locales = dict()
for i in range(count):
    name = input()
    locale = input()
    try:
        locales[locale] += 1
    except KeyError:
        locales[locale] = 1

for key, value in locales.items():
    print(key + " " + str(value))
