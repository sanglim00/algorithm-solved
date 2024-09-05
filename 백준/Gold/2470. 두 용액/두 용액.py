import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort(key= lambda x: abs(x))

min_ = float('INF')
minA, minB = 0, 0

for i in range(len(lst)-1):
    if min_ > abs(lst[i] + lst[i+1]):
        min_ = abs(lst[i] + lst[i+1])
        minA, minB  = lst[i], lst[i+1]

if minA < minB: print(minA, minB)
else: print(minB, minA)