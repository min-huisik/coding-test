
n = int(input())

d = [0]*(n+1)

d[1]= 0

for i in range(2, n+1):

    a = d[i-1]

    if i % 2 == 0:
        b = d[i//2]
    else:
        b= 1000001
    if i % 3 == 0:
        c = d[i//3]
    else:
        c = 1000001


    d[i]= min(a,b,c)+1

print(d[n])

