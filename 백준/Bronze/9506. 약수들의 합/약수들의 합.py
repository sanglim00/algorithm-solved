while True:
    N = int(input())
    if N == -1: break

    lst = []
    for i in range(1, N):
        if N % i == 0: lst.append(i)
    
    if sum(lst) == N:
        print(f"{N} =", end=' ')
        for i in range(len(lst)-1): print(f"{lst[i]} +", end=' ')
        print(lst[-1])
    else:
        print(f'{N} is NOT perfect.')