N = int(input())
lst = list(map(int, input().split()))

ans = 0
for i in lst:
    if i % 10 == N: ans += 1

print(ans)