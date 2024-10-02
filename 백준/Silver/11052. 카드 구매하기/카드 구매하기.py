

import sys

n = int(input())
lst = [0] + list(map(int, sys.stdin.readline().split()))

d = [0] * (n+1)

d[1] = lst[1]
d[2] = max(lst[2], lst[1]*2)

for i in range(3, n+1):
    d[i] = lst[i]
    for j in range(1, i//2 + 1):
        d[i] = max(d[i], d[j]+d[i-j])

print(d[n])