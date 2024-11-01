import sys

N = int(sys.stdin.readline())

now = 1000-N
lst = [500, 100, 50, 10, 5, 1]

ans = 0
for i in lst:
    ans += now // i
    now %= i

print(ans)