n = int(input())
ans = input()

adrian = 0
bruno = 0
goran = 0

for i in range (n):
    if i%3 == 0 and ans[i] == 'A':
        adrian += 1
    elif i%3 == 1 and ans[i] == 'B':
        adrian += 1
    elif i%3 == 2 and ans[i] == 'C':
        adrian += 1
    if i%4 == 0 and ans[i] == 'B':
        bruno += 1
    elif i%4 == 1 and ans[i] == 'A':
        bruno += 1
    elif i%4 == 2 and ans[i] == 'B':
        bruno += 1
    elif i%4 == 3 and ans[i] == 'C':
        bruno += 1
    if i%6 == 0 and ans[i] == 'C':
        goran += 1
    elif i%6 == 1 and ans[i] == 'C':
        goran += 1
    elif i%6 == 2 and ans[i] == 'A':
        goran += 1
    elif i%6 == 3 and ans[i] == 'A':
        goran += 1
    elif i%6 == 4 and ans[i] == 'B':
        goran += 1
    elif i%6 == 5 and ans[i] == 'B':
        goran += 1

# print(adrian,bruno,goran)        
max_score = max(adrian, bruno, goran)
print(max_score)

if adrian == max_score:
    print("Adrian")
if bruno == max_score:
    print("Bruno")
if goran == max_score:
    print("Goran")

    