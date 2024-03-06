import sys

num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
check = int(sys.stdin.readline())

print(lst.count(check))