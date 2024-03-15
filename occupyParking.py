a = int(input())
s1 = input()
s2 = input()
cnt = 0

for i in range (0,a):
    if s1[i] == "C" and s2[i] == "C": 
        cnt+=1
print(cnt)