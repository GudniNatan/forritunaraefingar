import math
class Sprengja(object):
    def __init__(self, (x, y, z), r):
        (self.x, self.y, self.z) = (x, y, z)
        self.r = r
        self.exploded = True

    def CollidesWith(self, other):
        dist = math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2) + math.pow(other.z - self.z, 2))
        """print (other.x, other.y, other.z, other.r)
        print (self.x, self.y, self.z, self.r)
        print dist"""
        if dist <= self.r + other.r:
            return True
        return False

class Geimskip(Sprengja):
    def __init__(self, (x, y, z), r):
        super(Geimskip, self).__init__((x, y, z), r)
        self.exploded = False

    def Explode(self):
        if not self.exploded:
            self.r *= 2
            self.exploded = True

n = int(raw_input())

skip = list()

for i in range(n):
    (x, y, z, r) = map(int, raw_input().split())
    skip.append(Geimskip((x, y, z), r))

sprengjufjoldi = int(raw_input())

for i in range(sprengjufjoldi):
    (x, y, z, r) = map(int, raw_input().split())
    skip.append(Sprengja((x, y, z), r))

while True:
    sprengingar = 0
    popIt = list()
    for i in range(len(skip)):
        if skip[i].exploded == True:
            for j in range(len(skip)):
                if j == i:
                    continue
                if skip[j].exploded == False and skip[i].CollidesWith(skip[j]):
                    skip[j].Explode()
                    sprengingar += 1
            popIt.append(i)
            #break
    popIt.reverse()
    #print popIt
    for i in range(len(popIt)):
        skip.pop(popIt[i])
    if sprengingar == 0:
        break

popIt = list()

"""for i in range(len(skip)):
    if skip[i].exploded == True:
        popIt.append(i)
        # break
for i in range(len(popIt)):
    skip.pop(popIt[i])"""

print(len(skip))
