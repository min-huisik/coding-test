import sys

n = int(sys.stdin.readline())

d=[]
d.append(0)
d.append(1)
d.append(2)

for i in range(3, n+1):
    #print(i)
    d.append((d[i-2] + d[i-1])%10007) 

print(d[n])