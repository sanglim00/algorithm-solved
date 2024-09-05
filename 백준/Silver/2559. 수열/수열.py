import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

i, j = 0, K
sum_ = sum(lst[:j])
max_ = sum_

while j < N:
    sum_ -= lst[i]
    i += 1
    sum_ += lst[j]
    max_ = max(max_, sum_)
    if j+1 < N: j+=1
    else:break

print(max_)