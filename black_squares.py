a = list(map(int,input().split()))
s = input()
total_calorie = 0
for char in s:
    if char == "1":
        total_calorie += a[0] 
    elif char == "2":
        total_calorie += a[1] 
    elif char == "3":
        total_calorie += a[2] 
    elif char == "4":
        total_calorie += a[3]
    else:
        total_calorie +=0
print(total_calorie)
