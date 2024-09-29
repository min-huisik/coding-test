import sys
from collections import deque

n = (map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
que = deque(lst)

min_val = 200000

while que:
    min_val = min((que.pop()+que.popleft()), min_val)


print(min_val)