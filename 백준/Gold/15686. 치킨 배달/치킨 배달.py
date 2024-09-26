import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

lst = []

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))


result =10000001
def cal_dis(a, b, c, d):
    return abs(c-a) + abs(d-b)


house = []
chicken = []

for i in range(n):
    for j in range(n):
        if lst[i][j]==1:
            house.append([i,j])
        elif lst[i][j]==2:
            chicken.append([i,j])


for chick in combinations(chicken, m):
    #print(chick)
    sv = 0
    for h in house:
        chi_len = 10000001
        for j in range(m):
            chi_len = min(cal_dis(chick[j][0], chick[j][1], h[0], h[1]), chi_len)
        sv += chi_len

    result = min(sv, result)

print(result)


