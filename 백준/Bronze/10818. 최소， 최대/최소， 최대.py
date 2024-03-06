import sys

num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

print(min(lst), max(lst))