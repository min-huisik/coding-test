


T = int(input())



def sol(n):

    d = []
    d.append([1, 0])
    d.append([0, 1])

    if n == 0:
        return (" ".join(map(str, d[0])))

    elif n == 1:
        return (" ".join(map(str, d[1])))

    else:
        for i in range(2, n+1):
            #print(i)
            val1 = d[i-1][0] + d[i-2][0]
            val2 = d[i-1][1] + d[i-2][1]
            d.append([val1, val2])

        return (" ".join(map(str, d[n])))

for _ in range(T):
    n = int(input())
    print(sol(n))
