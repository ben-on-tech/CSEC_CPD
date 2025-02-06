n = int(input())
magnets = []
group = 1
for i in range(n):
    magnet_side = input()
    magnets.append(magnet_side)
for j in range(1,n):
    if magnets[j] != magnets[j-1]:
        group += 1
print(group)

