def main():
    roksegd = raw_input().split("EDA")
    blocks = list()
    blockContents = list()
    okStill = False
    for r in roksegd:
        r = r.strip()
        breytur = dict()
        for b in r[1:-1].split("OG"):
            b = b.strip()
            if b[0] == "!":
                b = b[1:]
                try:
                    if breytur[b]:
                        blocks.append(False)
                        break
                except KeyError:
                    pass
                breytur[b] = False
            else:
                try:
                    if not breytur[b]:
                        blocks.append(False)
                        break
                except KeyError:
                    pass
                breytur[b] = True
        else:
            blocks.append(True)
            okStill = True
        blockContents.append(breytur)

    if not okStill:
        print "Neibb"
        return
    else:
        print "Jebb"
main()