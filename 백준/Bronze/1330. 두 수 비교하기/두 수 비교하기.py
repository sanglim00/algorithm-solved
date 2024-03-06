import sys

num, num2 = map(int, sys.stdin.readline().split())
print("<" if num < num2 else ">" if num > num2 else "==")