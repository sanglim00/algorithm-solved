import sys

N, K = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    A = int(sys.stdin.readline())
    lst.append(A)

lst.sort(reverse=True)

ans = 0
for i in lst:
    if K >= i:
        ans += K // i
        K %= i
        
print(ans)