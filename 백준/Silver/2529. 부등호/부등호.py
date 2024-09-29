import sys
from collections import deque

n = int(sys.stdin.readline().strip())
lst = list(map(str, sys.stdin.readline().split()))


visited = [False for _ in range(10)]

result = []


max_val = '0'
min_val = '9967843012'

def back(depth, par):
    global min_val, max_val
    if depth == n+1:
        val = (''.join(map(str, result)))
        num = int(val)

        if int(max_val) < num:
            max_val = val

        if int(min_val) > num:
            min_val = val

        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or (lst[depth-1] == '>' and par > i) or (lst[depth-1] == '<' and par < i):
                visited[i] = True
                result.append(i)
                back(depth+1, i)
                visited[i] = False
                result.pop()

back(0, -1)
print(max_val)
print(min_val)





