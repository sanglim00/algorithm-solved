import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

sum_ = [0 for _ in range(N+1)]
sum_[1] = lst[1]
for i in range(1, N+1):
    sum_[i] = sum_[i-1] + lst[i-1]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(sum_[end]-sum_[start-1])