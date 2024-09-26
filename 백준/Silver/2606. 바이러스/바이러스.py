import sys
from collections import deque

n = int(input())  # 컴퓨터의 수
k = int(input())  # 연결의 수

# 연결 리스트 초기화
lst = [ [0] * n for _ in range(n) ]
com_visited = [0] * n  # 방문 기록

# 연결 정보 입력
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    lst[a-1][b-1] = 1
    lst[b-1][a-1] = 1  # 연결은 양방향

# BFS 함수 정의
def bfs(start):
    que = deque([start])  # 시작점은 1번 컴퓨터 (0번 인덱스)
    com_visited[start] = 1  # 시작점 방문 처리

    while que:
        cur = que.popleft()  # 현재 컴퓨터
        for c in range(n):   # 연결된 모든 컴퓨터 탐색
            if lst[cur][c] == 1 and com_visited[c] == 0:  # 연결되어 있고 아직 방문하지 않은 경우
                que.append(c)  # 큐에 추가
                com_visited[c] = 1  # 방문 처리

# 1번 컴퓨터(0번 인덱스)부터 탐색 시작
bfs(0)

# 결과 출력 (1번 컴퓨터를 제외한 감염된 컴퓨터의 수)
print(sum(com_visited) - 1)
