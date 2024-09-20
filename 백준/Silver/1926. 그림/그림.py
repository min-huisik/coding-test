

def solution():
    n, m  = map(int, input().split())
    lst = [0 for _ in range(n)]

    for i in range(n):
        lst[i] = list(map(int, input().split()))

    visited = [[0] * m for _ in range(n)]

    que = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    num = 0
    mx = 0

    for i in range(n):
        for j in range(m):

            if lst[i][j] == 0 or visited[i][j] == 1:
                continue

            que.append([i,j])
            visited[i][j] = 1

            area = 0
            num += 1

            while que:
                area+=1
                cur = que.pop(0)

                for dir in range(4):
                    nx = cur[0]+dx[dir]
                    ny = cur[1]+dy[dir]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if visited[nx][ny] == 1 or lst[nx][ny] == 0:
                        continue

                    visited[nx][ny] = 1
                    que.append([nx, ny])
                    #print(que)

            mx = max(mx, area)

    print(num)
    print(mx)


solution()