import sys

num = int(sys.stdin.readline())
ans = 0

for i in range(1, num+1):
    ans = ans + i
print(ans)