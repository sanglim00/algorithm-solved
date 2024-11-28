N = int(input())
for i in range(1, N+1):
    lst = list(map(int, input().split()))

    new_lst = sorted(lst[1:])

    max_ = new_lst[-1]
    min_ = new_lst[0]
    gap_ = 0

    for j in range(1, lst[0]):
        gap_ = max(gap_, new_lst[j]-new_lst[j-1])

    print(f"Class {i}")
    print(f"Max {max_}, Min {min_}, Largest gap {gap_}" )