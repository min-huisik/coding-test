import sys




T = int(sys.stdin.readline().strip())
def sol():
    k = int(sys.stdin.readline().strip())
    lst = list(map(int, sys.stdin.readline().split()))
    mx = 0
    max_val = 0
    for i in range(k-1, -1, -1):
        if lst[i] > max_val:
            max_val = lst[i]
        mx += max_val - lst[i]

    return mx
for _ in range(T):
    print(sol())