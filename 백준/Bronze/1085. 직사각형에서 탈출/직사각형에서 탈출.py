import sys

x, y, w, h = map(int, sys.stdin.readline().split())
print(min(min(x - 0, y - 0), min(w - x, h - y)))