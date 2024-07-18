import sys

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    lst = []
    for _ in range(num):
        paper, interview = map(int, sys.stdin.readline().split())
        lst.append([paper, interview])

    lst.sort(key=lambda x: (x[0], x[1]))

    ans = 1
    now = lst[0][1]
    for i in range(1, len(lst)):
        if lst[i][1] < now:
            ans += 1
            now = lst[i][1]

    print(ans)