import sys

N = int(sys.stdin.readline())
for _ in range(N):
    str_ = sys.stdin.readline().split()
    
    for i in str_: print(i[::-1], end=' ')
    print()