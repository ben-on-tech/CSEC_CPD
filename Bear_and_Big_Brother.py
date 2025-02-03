weights = input()
i = 0
a,b = map(int,weights.strip().split())
while a  <= b:
    a*=3
    b*=2
    i+=1
print(i)
