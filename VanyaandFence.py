n_and_h = input().strip()
n, h = map(int, n_and_h.split())
min_width = 0
ais = list(map(int, input().strip().split()))
for height in ais:
    if height > h:
        min_width += 2 
    else:
        min_width += 1 
print(min_width)
