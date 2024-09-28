import sys

while True:

    lst= list(map(int, sys.stdin.readline().split()))

    if sum(lst)==0:
        break

    lst.sort()
    dic = {val : i for i,val in enumerate(lst)}

    if lst[0]+lst[1]<=lst[2]:
        print("Invalid")

    elif lst[0] == lst[1] == lst[2]:
        print("Equilateral")

    elif len(dic) == 2:
        print("Isosceles")

    else:
        print("Scalene")







