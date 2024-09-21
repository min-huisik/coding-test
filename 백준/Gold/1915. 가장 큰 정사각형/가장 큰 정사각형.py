

import sys


n, m = map(int, sys.stdin.readline().split())

lst = []

for _ in range(n):
    l = input().strip()
    lst.append([int(c) for c in l])

#print(lst)

dx = [-1,-1,0]
dy = [0,-1,-1]

for i in range(1, n):
    for j in range(1, m):
        if lst[i][j]!=0:
            #print(lst)
            lst[i][j] += min(lst[i + dx[dir]][j + dy[dir]] for dir in range(3))



result = max(map(max, lst))
print(result * result)