N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    sum_ = 0
    min_ = float("inf")
    for i in lst:
        if i % 2 == 0:
            sum_ += i
            min_ = min(min_, i)
    print(sum_, min_)