n = int(input())

d = [0] * (n + 1)
lst = [0] 
for i in range(n):
    lst.append(int(input()))

d[1] = lst[1]

if n >= 2:
    d[2] = lst[1] + lst[2]


for i in range(3, n + 1):
    d[i] = max(d[i-2] + lst[i], d[i-3] + lst[i-1] + lst[i])

print(d[n])