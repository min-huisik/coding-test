
import sys

n = int(input())

lst = list(map(int, sys.stdin.readline().split()))

lst = (sorted(list(set(lst))))


print(" ".join(map(str, lst)))