n = int(input())
k = n
a = int(input())
b = int(input())
c = int(input())
total_play = 0

while k>0:
    a += 1
    k -= 1
    total_play += 1
    if a%35 == 0:
        k += 30
    if k == 0:
        break

    b += 1
    k -= 1 
    total_play += 1
    if b%100 == 0:
        k += 60
    if k == 0:
        break
    
    c += 1
    k -= 1
    total_play += 1
    if c%10 == 0:
        k += 9
    if k == 0:
        break

print("Martha plays",total_play,"times before going broke.")

    
    