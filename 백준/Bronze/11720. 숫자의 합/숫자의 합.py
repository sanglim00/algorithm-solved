import sys

num = int(sys.stdin.readline())
check = sys.stdin.readline()

ans = 0
for i in range(0, num): ans += int(check[i])
print(ans)

 