import sys

A, B = sys.stdin.readline().rstrip().split()
A = A[::-1]
B = B[::-1]
ans = str(int(A)+int(B))
ans = ans[::-1]
print(int(ans))