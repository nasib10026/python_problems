string = input()
loc = 1
for i in string:
    if i == 'A' and loc == 1:
        loc = 2
        
    elif i == 'A' and loc == 2:
        loc = 1
     
    elif i == 'B' and loc == 2:
        loc = 3
        
    elif i == 'B' and loc == 3:
        loc = 2
        
    elif i == 'C' and loc == 1:
        loc = 3
        
    elif i == 'C' and loc == 3:
        loc = 1
        

print(loc)
