import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
max_ = max(score)

ans = 0
for i in score: ans += i / max_ * 100
print(ans/N)