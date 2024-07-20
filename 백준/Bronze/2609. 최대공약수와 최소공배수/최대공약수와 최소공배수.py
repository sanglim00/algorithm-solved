import sys

N, M = map(int, sys.stdin.readline().split())

def GCD(n, m):
    while m:
        n, m = m, n%m
    return n

def LCM(n, m):
    ans = n*m // GCD(n, m)
    return ans

print(GCD(N, M))
print(LCM(N, M))