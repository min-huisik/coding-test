from collections import deque
import sys

T = int(sys.stdin.readline())

def solution():
    prom = sys.stdin.readline().strip()

    n = int(sys.stdin.readline())

    # 빈 배열일 때 처리
    input_string = sys.stdin.readline().strip()
    if n == 0:
        int_lst = []
    else:
        int_lst = list(map(int, input_string.strip('[]').split(',')))

    lst = deque(int_lst)

    state = 1
    len_prom = len(prom)

    for i in range(len_prom):
        if prom[i] == 'R':
            state *= -1
        elif prom[i] == 'D':
            if not lst:
                return 'error'
            if state == 1:
                lst.popleft()
            else:
                lst.pop()

    # 상태가 뒤집힌 경우 리스트를 반전
    if state == -1:
        lst.reverse()

    return list(lst)

for _ in range(T):
    result = solution()
    if result == 'error':
        print(result)
    else:
        print(f"[{','.join(map(str, result))}]")
