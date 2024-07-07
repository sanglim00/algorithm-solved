import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lst.append([start, end])

lst.sort(key=lambda a: (a[1], a[0]))

ans = 0
point = 0
for start, end in lst:
    if point <= start: 
        point = end
        ans += 1

print(ans)