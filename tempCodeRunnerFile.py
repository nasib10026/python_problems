a = int(input())
b = int(input())
c = int(input())
d = int(input())

f=0

if a!=8 or a!=9:
    f=1
if b!=c:
    f=1
if d!=8 or d!=9:
    f=1

if f==0:
    print("ignore")
else:
    print("answer")