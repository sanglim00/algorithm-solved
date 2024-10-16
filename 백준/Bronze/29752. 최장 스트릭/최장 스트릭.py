N = int(input())
lst = list(map(int, input().split()))

ans = 0
cnt = 0
for i in lst:
    if i > 0:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)