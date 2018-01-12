t = int(raw_input())

joinIt = "".join

for x in xrange(t):
    n = int(raw_input())
    people = dict()
    for j in xrange(n):
        asd = raw_input().split()
        name = asd[0][:-1]
        classes = asd[1].split('-')
        classes.reverse()
        classLevel = list()
        for c in classes:
            if c == "upper":
                classLevel.append("0")
            if c == "middle":
                classLevel.append("1")
            if c == "lower":
                classLevel.append("2")
        for a in xrange(10 - len(classes)):
            classLevel.append("1")
        classLevelString = joinIt(classLevel)
        people[name] = int(classLevelString)

    for key, value in sorted(people.iteritems(), key=lambda (k, v): (v, k)):
        print key
    print "=============================="