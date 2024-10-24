N, K = map(int, input().split())

lst = [i for i in range(N+1)]
lst[0] = 0
lst[1] = 0

for i in range(2, N+1):
    if K == 0: break
    for j in range(i, N+1, i):
        if lst[j] == 0: continue

        lst[j] = 0
        K -= 1
        if K == 0:
            print(j)
            break