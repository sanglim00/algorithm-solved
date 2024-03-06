import sys

p = int(sys.stdin.readline())
q = int(sys.stdin.readline())

if p > 0 and q > 0: print(1)
elif p > 0 and q < 0 : print(4)
elif p < 0 and q > 0: print(2)
else: print(3)
