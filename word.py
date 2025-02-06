s = input()
i=0
j=0
for char in s:
    if char.islower():
        i +=1
    else:
        j +=1
if i >= j:
    print(s.lower())
else:
    print(s.upper())
