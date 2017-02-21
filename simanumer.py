numerafjoldi = int(raw_input())

simaskra = list()
simanumerEftirUpphafstofum = [list() for x in range(10)]
simanumerEftir2Upphafstofum = [list() for x in range(100)]
simanumerEftir3Upphafstofum = [list() for x in range(1000)]
for i in range(numerafjoldi):
    simaskra.append(raw_input())
    simanumerEftirUpphafstofum[int(simaskra[i][0])].append(simaskra[i])
    simanumerEftir2Upphafstofum[int(simaskra[i][0: 2])].append(simaskra[i])
    simanumerEftir3Upphafstofum[int(simaskra[i][0: 3])].append(simaskra[i])
fyrirspurnafjoldi = int(raw_input())

for i in range(fyrirspurnafjoldi):
    tala = 0
    fyrirspurn = raw_input()
    if len(fyrirspurn) == 1:
        for numer in simanumerEftirUpphafstofum[int(fyrirspurn[0])]:
            if numer[0: len(fyrirspurn)] == fyrirspurn:
                tala += 1
    elif len(fyrirspurn) == 2:
        for numer in simanumerEftir2Upphafstofum[int(fyrirspurn[0: 2])]:
            if numer[0: len(fyrirspurn)] == fyrirspurn:
                tala += 1
    else:
        for numer in simanumerEftir3Upphafstofum[int(fyrirspurn[0: 3])]:
            if numer[0: len(fyrirspurn)] == fyrirspurn:
                tala += 1
    print tala