import sys

bill = int(sys.stdin.readline())
num = int(sys.stdin.readline())

ans = 0
for i in range(0, num):
    a, b = map(int, sys.stdin.readline().split())
    ans = ans + a*b

print("Yes" if bill == ans else "No")