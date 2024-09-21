import sys
import heapq

n = int(input())

heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    heapq.heappush(heap, x)

result = 0
while True:

    if len(heap) == 1:
        print(result)
        break

    else:
        sum = heapq.heappop(heap) + heapq.heappop(heap)
        result += sum
        heapq.heappush(heap, sum)





