import sys
from collections import deque


n = int(sys.stdin.readline())

lst =[list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
que = deque()
num = 0
area_lst =[]

for i in range(n):
    for j in range(n):

        if visited[i][j] == 0 and lst[i][j] == 1:
            que.append([i,j])
            visited[i][j] =1
            area = 0
            num +=1
            while que:
                area += 1
                cur = que.popleft()
                cx = cur[0]
                cy = cur[1]
                for dir in range(4):
                    nx = cx + dx[dir]
                    ny = cy + dy[dir]

                    if 0<= nx < n and 0 <= ny <n:
                        if visited[nx][ny]==0 and lst[nx][ny]==1:
                            que.append([nx, ny])
                            visited[nx][ny]=1

            area_lst.append(area)

area_lst.sort()
print(num)
for l in area_lst:
    print(l)
