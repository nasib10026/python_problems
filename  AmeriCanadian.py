vowels = ['a', 'e', 'i', 'o', 'u','y']

while True:
    word = input()
    k = len(word)
    if word == 'quit!':
        break
    if k > 4 and word[-2:] == 'or' and word[-3] not in vowels:
       print(word[0:-2] +"our")
    
    else:
       print(word)

