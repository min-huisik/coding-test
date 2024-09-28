
n =int(input())
lst = [int(input()) for _ in range(n)]

lst.sort(reverse=True)

result = lst[-1] * n


for i in range(n):
    result = max(result, lst[i]*(i+1))


print(result)