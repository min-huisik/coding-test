import sys

n, s = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

#print(n, s, lst)

result = []

count = 0

def back(start, depth, target):
    global count
    if depth == target and sum(result)==s:
        count +=1
        return

    for i in range(start, n):
        result.append(lst[i])
        back(i+1, depth+1, target)
        result.pop()

for l in range(1, n+1):
    back(0, 0, l)

print(count)
