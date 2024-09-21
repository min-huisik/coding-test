import sys
from collections import deque

n, m = map(int, input().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

time = 0

ice_positions = [(i, j) for i in range(n) for j in range(m) if lst[i][j] > 0]

def bfs(x, y):
    que = deque([(x, y)])
    visited[x][y] = True

    while que:
        cur_x, cur_y = que.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if 0 <= nx < n and 0 <= ny < m:
                if lst[nx][ny] == 0 and lst[cur_x][cur_y] > 0:
                    melting[cur_x][cur_y] += 1
                elif not visited[nx][ny] and lst[nx][ny] > 0:
                    que.append((nx, ny))
                    visited[nx][ny] = True

while True:
    count = 0
    visited = [[False] * m for _ in range(n)]
    melting = [[0] * m for _ in range(n)]

    # 각 빙산 덩어리를 BFS로 탐색
    for i, j in ice_positions:
        if lst[i][j] > 0 and not visited[i][j]:
            bfs(i, j)
            count += 1

    # 빙산을 녹이는 과정
    new_ice_positions = []
    for i, j in ice_positions:
        lst[i][j] = max(0, lst[i][j] - melting[i][j])
        if lst[i][j] > 0:  # 녹지 않고 남은 빙산 위치 추적
            new_ice_positions.append((i, j))

    if count >= 2:
        print(time)
        break


    if not new_ice_positions:
        print(0)
        break

    ice_positions = new_ice_positions
    time += 1
