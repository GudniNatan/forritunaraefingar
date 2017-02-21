class Dansari:
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def __str__(self):
        return str(self.value)


def main():
    input1 = raw_input().split()
    input2 = raw_input().split()
    staedi = map(int, input2)
    fjoldi = int(input1[0])
    umferdir = int(input1[1])
    dansarar = list()
    for i in range(fjoldi):
        dansarar.append(Dansari(i + 1, i + 1))
    asd = umferdir % fjoldi
    if asd == 0 and umferdir != 0:
        asd = fjoldi
    for i in range(asd):
        for j in range(fjoldi):
            dansarar[staedi[j] - 1].position = j
        dansarar.sort(key=lambda x: x.position)
        """strengur = ""
        for dansari in dansarar:
            strengur += str(dansari) + " "
        print strengur[0: -1]"""
    strengur = ""
    for dansari in dansarar:
        strengur += str(dansari) + " "
    print strengur[0: -1]

main()