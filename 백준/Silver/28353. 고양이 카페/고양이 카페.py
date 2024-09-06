import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()


ans = 0
i, j = 0, N-1

while i<j:
    if lst[i]+lst[j] <=K:
        ans += 1
        i += 1
    j -=1
        

print(ans)