n = int(raw_input())

dictionary = dict()
splitIt = str.split

for i in range(n):
    skipun = splitIt(raw_input())
    if skipun[0] == "INNTAK":
        dictionary[skipun[1]] = True if skipun[2] == "SATT" else False
    elif skipun[0] == "UTTAK":
        print skipun[1] + " " + ("SATT" if dictionary[skipun[1]] else "OSATT")
    elif skipun[0] == "EKKI":
        dictionary[skipun[2]] = not dictionary[skipun[1]]
    elif skipun[0] == "OG":
        dictionary[skipun[3]] = dictionary[skipun[1]] and dictionary[skipun[2]]
    elif skipun[0] == "EDA":
        dictionary[skipun[3]] = dictionary[skipun[1]] or dictionary[skipun[2]]