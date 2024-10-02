

import sys

n = int(input())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#print(lst)
visited = [False] * n


end_len = n//2
min_val = 999999999
def back(depth, start):
    global min_val
    if depth == end_len:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += lst[i][j]
                elif not visited[i] and not visited[j]:
                    b += lst[i][j]
        min_val = min(min_val, abs(a-b))
        #print(min_val)
        return


    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            back(depth+1, i + 1)
            visited[i] = False


back(0, 0)
print(min_val)