from fractions import Fraction
line = input()
y,w= map(int,line.split())
max = max(y, w)
outcomes = 6 - max + 1
probability = Fraction(outcomes, 6)
if outcomes == 6:
    print("1/1")
elif outcomes == 0:
    print("0/1")
else:
    print(probability)
