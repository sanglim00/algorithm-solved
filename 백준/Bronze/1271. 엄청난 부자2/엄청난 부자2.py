import sys

n, m = list(map(int, sys.stdin.readline().split()))
print(list(divmod(n, m))[0])
print(list(divmod(n, m))[1])