n = int(input())
s = list(map(int, input().split()))
police = 0
untreated = 0

for event in s:
    if event > 0:
        police += event
    else:
        if police > 0:
            police -= 1  
        else:
            untreated += 1  

print(untreated)
