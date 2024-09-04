import sys

N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

check = False
for i in lst:
    if i >= S: check = True

if check: print(1)
else:
    i, j = 0, 1
    ans = []
    sum_= sum(lst[:j+1])
    while j < N:
        if sum_ < S:
            if j+1 < N:
                j += 1
                sum_ += lst[j]
            else: break
        else:
            ans.append(j-i+1)
            sum_ -= lst[i]
            i += 1
    print(min(ans) if ans else 0)