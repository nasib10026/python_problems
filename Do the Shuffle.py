songs = 'ABCDE'
buttons = 0

while buttons != 4:
    buttons = int(input())
    presses = int(input())

    for i in range(presses):
        if buttons == 1:
            songs = songs[1:]+songs[0]
        elif buttons == 2:
            songs = songs[-1]+songs[:-1]
        elif buttons == 3:
            songs = songs[1]+songs[0]+songs[2:]
    
ans = ''

for i in songs:
    ans += i + " "

print(ans[:-1])
