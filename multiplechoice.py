a = int(input())
k = 2*a 
ans = ""
cnt = 0
for _ in range(k):
    b = input()
    ans += b

for i in range(0,a):
    if ans[i] == ans[i+a]:
        cnt+=1 
print(cnt)