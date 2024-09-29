import sys

s, n = map(int, sys.stdin.readline().split())
lst = list(map(str, sys.stdin.readline().split()))

#print(n, s, lst)

lst.sort()
#print(lst)
result = []


def back(start, depth):
    global count
    if depth == s:
        count = [0, 0]
        for r in result:
            if r in ['a','e','i','o','u']:
                count[0] += 1
            else:
                count[1] += 1
        if count[0] >= 1 and count[1]>=2:
            print("".join(map(str, result)))
        return

    for i in range(start, n):
        result.append(lst[i])
        back(i+1, depth+1)
        result.pop()


back(0, 0)


