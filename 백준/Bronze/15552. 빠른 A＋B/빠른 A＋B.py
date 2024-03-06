import sys

num = int(sys.stdin.readline())

for i in range(0, num):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)