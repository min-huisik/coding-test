import sys


n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
idxs = [i for i in range(n)]


start = 0
end = max(lst)

result = 0

while start <=end:
    mid = (start+end)//2
    
    total = 0
    for l in lst:
        if l > mid:
            total += l - mid
    
    if total >= m:
        result = mid
        start = mid + 1
        
    else:
        end = mid-1

print(result)