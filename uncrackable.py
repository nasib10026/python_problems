password = input()

length = len(password)
lower = 0
upper = 0
digit = 0

if length < 8 or length > 12:
    print("Invalid")
else:
    for i in password:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i>='0' and i<='9':
            digit+=1
    
    if upper>=2 and lower>=3 and digit >= 1:
        print("Valid")
    else:
        print("Invalid")