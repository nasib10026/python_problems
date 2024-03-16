a_cnt = 1
b_cnt = 0

k = int(input())

for i in range (0,k):
    tmp = b_cnt
    b_cnt += a_cnt 
    a_cnt = tmp

print(a_cnt,b_cnt)