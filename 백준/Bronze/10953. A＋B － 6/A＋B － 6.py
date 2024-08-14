import sys

N = int(sys.stdin.readline())
for _ in range(N):
    AB = sys.stdin.readline().strip()
    A, B = AB.split(',')
    print(int(A)+int(B))