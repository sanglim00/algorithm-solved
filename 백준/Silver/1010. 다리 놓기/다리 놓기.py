import sys

num = int(sys.stdin.readline())

def factorial(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i
    return ans

for _ in range(num):
    N, M = map(int, sys.stdin.readline().split())

    ans = factorial(M) // (factorial(M-N) * factorial(N))
    print(ans)
    