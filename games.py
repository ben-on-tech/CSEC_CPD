n = int(input())
uniforms = []
for _ in range(n):
    home, guest = map(int, input().split())
    uniforms.append((home, guest))

home_uniforms = []
guest_uniforms = []
changes = 0
for uniform in uniforms:
    home_uniforms.append(uniform[0]) 
    guest_uniforms.append(uniform[1]) 
    
for home in home_uniforms:
        for guest in guest_uniforms:
            if home == guest:  
                changes += 1  

print(changes)
