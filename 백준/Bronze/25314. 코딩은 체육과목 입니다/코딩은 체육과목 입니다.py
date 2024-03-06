import sys

num = int(sys.stdin.readline())

ans = ""
for i in range(0, num // 4):
    ans += "long "
ans += "int"

print(ans)