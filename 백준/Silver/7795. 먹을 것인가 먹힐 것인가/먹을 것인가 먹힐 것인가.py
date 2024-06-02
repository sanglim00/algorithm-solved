import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    ans = 0
    i, j = 0, 0
    while i < n and j < m:
        if a[i] > b[j]:
            ans += m-j
            i += 1
        else: j += 1
    

    print(ans)
