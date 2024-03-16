s = input()
king = s
obey = 1
t = int(input())
while t > 0:
    s1, s2 = input().split()
    if s2 == king:
        king = s1
        obey += 1
    t -= 1
print(king)
print(obey)