#Ekki full lausn
numerafjoldi = int(raw_input())

simaskra = list()
for i in range(numerafjoldi):
    simaskra.append(raw_input())

fyrirspurnafjoldi = int(raw_input())

for i in range(fyrirspurnafjoldi):
    tala = 0
    fyrirspurn = raw_input()
    for numer in simaskra:
        if numer[0: len(fyrirspurn)] == fyrirspurn:
            tala += 1
print tala