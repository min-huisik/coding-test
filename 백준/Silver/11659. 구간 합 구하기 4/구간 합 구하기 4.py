

import sys

l, t = map(int, sys.stdin.readline().split())

lst =[0]+list(map(int, sys.stdin.readline().split()))

#print(l, t)
#print(lst)

d=[0]*(l+1)
for i in range(1,len(lst)):
    d[i]=d[i-1]+lst[i]

#print(d)

for _ in range(t):
    s, e = map(int, sys.stdin.readline().split())

    print(d[e]-d[s-1])

