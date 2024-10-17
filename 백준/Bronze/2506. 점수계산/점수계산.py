N = int(input())
lst = list(map(int, input().split()))

ans = 0
now = 1
for i in range(N):
    if lst[i]:
        ans += now
        now += 1
    else:
        now = 1
print(ans)