s = input()
t = input()
pos = 0
for i in range(len(t)):
    if pos < len(s) and t[i] == s[pos]:
        pos += 1
print(pos + 1)
