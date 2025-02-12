line = input()
horseshoe = list(map(int,line.split()))
leftover = set(horseshoe)
print(4 - len(leftover))
