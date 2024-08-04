import sys

N, M = map(int, sys.stdin.readline().split())
S = []

for _ in range(N):
    str_ = sys.stdin.readline().rstrip()
    S.append(str_)

ans = 0
for _ in range(M):
    str_ = sys.stdin.readline().rstrip()
    if str_ in S:
        ans+=1

print(ans)

