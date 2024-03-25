num = int(input())
take = 0
serve = 0
while True:
    s = input()
    if s == "EOF":
     break
    elif s == "TAKE":
       take += 1
       num += 1
       if num > 999:
           num = 1
    elif s == "SERVE":
       serve += 1
       
    elif s == "CLOSE":
       print(take,take-serve,num)
       take = 0
       serve = 0 

