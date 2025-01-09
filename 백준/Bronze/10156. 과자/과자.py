K, N, M = map(int, input().split())
money = K * N
if money > M:
    print(money-M)
else:
    print(0)