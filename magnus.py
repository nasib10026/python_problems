desired = "HONI"

string = input()
j = 0
cnt = 0
for i in string:
    if i == desired[j]:
        j += 1
        if j == 4:
            cnt += 1
            j = 0
        else:
            continue
   

print(cnt)