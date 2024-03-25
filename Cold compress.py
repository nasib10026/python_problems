t = int(input())

for _ in range(t):
    s = input()
    k = len(s)
    cnt = 0
    i = 0
    while i < k:
        if i < k-1 and s[i] == s[i + 1]:
            cnt += 1
        else:
            print(cnt + 1, s[i], end=" ")
            cnt = 0
        i += 1
    print()
