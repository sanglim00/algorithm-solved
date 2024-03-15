import sys

A, B, C = list(map(int, sys.stdin.readline().split()))

if B > C or C-B == 0 : print(-1)
else: print(A//(C-B)+1)
            

