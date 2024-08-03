import sys

A, B = sys.stdin.readline().split()
print(A[::-1] if A[::-1] > B[::-1] else B[::-1])
