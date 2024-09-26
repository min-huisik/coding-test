import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

lst = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
que = deque()

# 불이 퍼진 시간을 저장할 배열
fire_time = [[-1] * m for _ in range(n)]


def bfs_fire():
    # 불이 시작되는 모든 위치에서 BFS 시작
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 'F':
                que.append((i, j))
                fire_time[i][j] = 0

    while que:
        cx, cy = que.popleft()
        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == '.' and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[cx][cy] + 1
                que.append((nx, ny))


def bfs_person():
    visited = [[-1] * m for _ in range(n)]

    # J(사람)에서 BFS 시작
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 'J':
                que.append((i, j))
                visited[i][j] = 0

    while que:
        cx, cy = que.popleft()

        # 사람이 가장자리에 도달하면 탈출 성공
        if cx == 0 or cy == 0 or cx == n - 1 or cy == m - 1:
            return visited[cx][cy] + 1

        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]

            if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == '.' and visited[nx][ny] == -1:
                # 불이 아직 퍼지지 않았거나, 불이 퍼지기 전에 도착할 수 있는 경우
                if fire_time[nx][ny] == -1 or visited[cx][cy] + 1 < fire_time[nx][ny]:
                    visited[nx][ny] = visited[cx][cy] + 1
                    que.append((nx, ny))

    return "IMPOSSIBLE"  # 탈출 실패 시


# 불이 퍼지는 시간 계산
bfs_fire()

# 사람이 탈출하는 경로 계산
result = bfs_person()
print(result)
