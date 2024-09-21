

n = int(input())

lst=[0]

for _ in range(n):
    lst.append(int(input()))

d=[0]

if n>0:
    d.append(lst[1])
if n>1:
    d.append(lst[1]+lst[2])

if n>2:
    for i in range(3, len(lst)):
        a = max(d[i-2]+lst[i], d[i-3] + lst[i-1] + lst[i])
        d.append(max(a, d[i-1]))

print(d[n])
