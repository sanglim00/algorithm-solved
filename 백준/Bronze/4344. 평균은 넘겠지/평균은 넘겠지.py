import sys

C = int(sys.stdin.readline())
for _ in range(C):
    N_lst = list(map(int, sys.stdin.readline().split()))

    mean = round(sum(N_lst[1:]) / N_lst[0], 3)
    
    sum_ = 0
    for i in range(1, N_lst[0]+1):
        if N_lst[i] > mean:
            sum_ += 1
            
    print(f"{format(round(sum_ / N_lst[0] * 100, 3), '.3f')}%")