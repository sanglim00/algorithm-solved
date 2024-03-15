import sys

num, num2 = list(sys.stdin.readline().split())
ans = 0
num = list(map(int, num.replace('0', '')))
num2 = list(map(int, num2.replace('0', '')))

for i in num: ans += sum(num2) * i
print(ans) 