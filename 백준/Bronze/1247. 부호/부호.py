import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())

    ans = 0
    for _ in range(N):
        num = int(input())
        ans += num
    
    if ans > 0: print('+')
    elif ans == 0: print(0)
    else: print('-')