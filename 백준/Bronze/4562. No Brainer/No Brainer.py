N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    if X >= Y:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')
