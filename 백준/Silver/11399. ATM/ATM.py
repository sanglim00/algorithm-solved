import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

ans = 0
plus = 0

for i in range(len(lst)):
    plus += lst[i]
    ans += plus
print(ans)

