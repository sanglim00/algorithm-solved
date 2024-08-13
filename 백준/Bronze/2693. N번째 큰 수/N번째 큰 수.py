import sys

N = int(sys.stdin.readline())
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    print(lst[-3])