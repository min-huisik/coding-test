import sys

n = int(input())

lst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x,y])

lst.sort(key=lambda x: (x[1], x[0]))

for l in lst:
    print(" ".join(map(str, l)))