import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    lst.append((t, p))

dp = [0 for _ in range(N)]
cnt = [1 for _ in range(N)]
dp[0] = lst[0][1] if lst[0][0] <= N else 0
cnt[0] = 1 if lst[0][0] <= N else 0

for i in range(1, N):
    if i+lst[i][0] > N: continue
    dp[i] = lst[i][1]
    for j in range(i):
        if j+lst[j][0]> i: continue
        if dp[i] < dp[j]+lst[i][1]:
            dp[i] = dp[j]+lst[i][1]
            cnt[i] = cnt[j]+1

ans = 0
idx = -1
for i in range(len(cnt)):
    if idx <= cnt[i]:
        idx = cnt[i]
        ans = max(ans, dp[i])

print(ans)