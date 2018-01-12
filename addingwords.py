coolDict = dict()
#coolArr = [0 for i in xrange(2500)]

joinIt = " ".join

while True:
    inputString = None
    try:
        inputString = raw_input().split()
    except EOFError:
        break
    if inputString is None:
        break
    if inputString[0] == "def":
        coolDict[inputString[1]] = inputString[2]
        #coolArr[int(inputString[2]) + 1200] = inputString[1]
    if inputString[0] == "clear":
        coolDict = dict()
        #coolArr = [0 for i in xrange(2500)]
    if inputString[0] == "calc":
        inputString = inputString[1: -1]
        asd = joinIt(inputString)
        calculationString = ""
        for s in inputString:
            if s in ("+", "-"):
                calculationString += s
            else:
                try:
                    calculationString += coolDict[s]
                except KeyError:
                    calculationString = "NOPE"
                    break
        if calculationString != "NOPE":
            val = eval(calculationString)
            #print val
            #print coolArr
            if val <= 1000 and val >= -1000:
                try:
                    bla = coolDict.keys()[coolDict.values().index(str(val))]
                    #print asd + " = " + str(coolArr[val + 1200])
                    print asd + " = " + bla
                    continue
                except ValueError:
                    pass
        print asd + " = unknown"
