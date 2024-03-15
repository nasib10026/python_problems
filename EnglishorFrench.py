n = int(input())
t_count = 0
s_count = 0

for _ in range(n):
    s = input()
    k = len(s)
    for i in range(k):
        if s[i] == 't' or s[i] == 'T':
            t_count += 1
        elif s[i] == 's' or s[i] == 'S':
            s_count += 1

if t_count > s_count:
    print("English")
elif s_count > t_count:
    print("French")
else:
    print("French")
