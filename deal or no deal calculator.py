n = int(input())

list1 = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
total = 0
for i in range(len(list1)):
    total += list1[i]

for _ in range(n):
      k = int(input())
      total -= list1[k-1]

avg = total/(10 - n)

deal = float(input())

if deal > avg:
    print("deal")
else :
    print("no deal")