a = int(input())
b = int(input())
sum_val = 0
for _ in range(b):
    k = int(input())
    sum_val += k
print((a * b) - sum_val + a)
