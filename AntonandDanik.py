n = int(input())
gamewon = input()
anton = 0
danik = 0
for char in gamewon:
    if char == "A":
        anton += 1
    else:
        danik += 1
if anton > danik:
    print("Anton")
elif anton < danik:
     print("Danik")
else:
    print("Friendship")

