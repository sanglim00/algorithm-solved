N = int(input())
for _ in range(N):
    num = int(input())
    ans = 0
    for i in range(1, num+1):
        now = 0
        for j in range(1, i+2):
            now += j
        ans += now*i
    print(ans)