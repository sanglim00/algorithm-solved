import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)

K = int(sys.stdin.readline())
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans=0
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            ans += arr[i][j]
    print(ans)
