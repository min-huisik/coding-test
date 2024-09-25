import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

cap = int(sys.stdin.readline())


low, high = 0, max(lst)  # 최소, 최대

answer = 0  # 최종 정답 저장
while low <= high:
    total = 0
    mid = (low + high) // 2  # 중간값

    for num in lst:  # 예산에 따라 추가
        total += min(num, mid)

    if total <= cap:  # 한도를 넘지 않는 경우
        low = mid + 1
        answer = mid
    else:  # 한도 초과인 경우
        high = mid - 1

print(answer)

