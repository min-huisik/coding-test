
n = int(input())
lst = input().split(" ")
lst = list(map(int, lst))

d = [0]
d[0] = lst[0]
for i in range(1, n):
    d.append(max(lst[i], d[i-1]+ lst[i]))

print(max(d))