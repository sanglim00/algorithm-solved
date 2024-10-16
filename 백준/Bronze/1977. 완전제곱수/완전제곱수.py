M = int(input())
N = int(input())

start = 1
now = start**2

ans = []
while now <= N:
    if M <= now <= N:
        ans.append(now)
    start += 1
    now = start**2

if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)