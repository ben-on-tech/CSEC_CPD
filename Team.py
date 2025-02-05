n = int(input())
v = None
v3=0
for i in range(n):
    v = input()
    v2 = 0
    for char in v:
        if char == "1":
            v2 += 1
        else:
            v2 += 0
    if v2 >= 2:
        v3 += 1
print(v3)
    
