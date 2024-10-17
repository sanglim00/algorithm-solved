N = int(input())
lst = list(map(int, input().split()))

ans = []
for i in range(N):
    ans.insert(lst[i], i+1)

for i in range(N-1, -1, -1):
    print(ans[i], end=' ')
print()