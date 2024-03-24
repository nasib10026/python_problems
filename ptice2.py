n = int(input())
ans = input()

adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

scores = {'Adrian': 0, 'Bruno': 0, 'Goran': 0}

for i in range(0,n):
    if ans[i] == adrian[i % 3]:
        scores['Adrian'] += 1
    if ans[i] == bruno[i % 4]:
        scores['Bruno'] += 1
    if ans[i] == goran[i % 6]:
        scores['Goran'] += 1

max_score = max(scores.values())

print(max_score)

for name, score in scores.items():
    if score == max_score:
        print(name)
