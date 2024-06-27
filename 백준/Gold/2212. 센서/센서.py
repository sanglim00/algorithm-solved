import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst = list(set(lst))
lst.sort()

if N <= K:
    print(0)
else:
    cost = []
    for i in range(1, len(lst)):
        cost.append(lst[i]-lst[i-1])
    for i in range(K-1):
        cost.remove(max(cost))
    print(sum(cost))