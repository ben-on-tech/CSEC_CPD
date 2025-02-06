name = input()
letter = 'a'
steps = 0
for char in name:
    clock = abs(ord(char)-ord(letter))
    counter = 26 - clock
    steps += min(clock,counter)
    letter = char
print(steps)
