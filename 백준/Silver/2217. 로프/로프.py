import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
lst.sort()

max_ = lst[0] * N
for i in range(1, N-1):
    max_ = max(lst[i] * (N-i), max_)

print(max(max_, lst[-1]))