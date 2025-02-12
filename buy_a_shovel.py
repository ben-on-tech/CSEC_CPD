def min_shovels(k, r):
    for i in range(1, 11):
        if (k * i) % 10 == 0 or (k * i) % 10 == r:
            return i
k, r = map(int, input().split())

print(min_shovels(k, r))
