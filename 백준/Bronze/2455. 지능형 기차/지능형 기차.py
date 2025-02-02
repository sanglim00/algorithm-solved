ans = 0
before = 0
for _ in range(4):
    X, Y = map(int, input().split())
    before = before-X
    ans = max(ans, before+Y)
    before += Y

print(ans)