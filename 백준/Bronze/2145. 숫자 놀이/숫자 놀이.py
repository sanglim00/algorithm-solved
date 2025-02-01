while True:
    N = input().rstrip()
    if N == '0': break

    ans = N
    while len(ans) != 1:
        sum_ = 0
        for i in ans: sum_ += int(i)
        ans = str(sum_)
    print(ans)