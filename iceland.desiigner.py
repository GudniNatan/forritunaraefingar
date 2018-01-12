s = raw_input()

serhljodar = ["a", "e", "i", "o", "u", "y"]
if len(s) > 3 and s[:3] == "brr" and s[-2] == "r" and s[-1] in serhljodar:
    print "Jebb"
else:
    print "Neibb"