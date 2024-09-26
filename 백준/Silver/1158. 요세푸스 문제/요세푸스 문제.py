from collections import deque

n, k = map(int, input().split())


que = deque()

for i in range(n):
    que.append(i+1)
print("<", end="")
while que:
    for _ in range(k-1):
        que.append(que.popleft())
    if len(que) == 1:
        print(str(que.popleft())+">")
    else:
        print(str(que.popleft())+", ", end="")
