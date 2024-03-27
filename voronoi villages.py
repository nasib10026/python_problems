n = int(input())
b = []
for _ in range(n):
    pos = int(input())
    b.append(pos)

b.sort()
    
mini = (b[2] - b[0]) / 2 
for i in range(1, n - 1):
    x = (b[i + 1] - b[i - 1]) / 2  
    mini = min(mini, x)  

print(mini)