P = int(input())
N = int(input())
R = int(input())
day_cnt = 0
infected = N 
infected_total = N

while True:
    if infected_total > P:
        print(day_cnt)
        break
    infected = infected * R
    infected_total += infected
    day_cnt += 1


