vowels = ['a','e','i','o','u']

secret = input()
decode = ''
length = len(secret)
i = 0

while i<length:
    if secret[i] in vowels and i+1<length and i+2<length and secret[i]==secret[i+2] and secret[i+1]=='p':
        decode+=secret[i]
        i+=3
    else:
        decode+=secret[i]
        i+=1
print(decode)
