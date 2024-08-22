import sys

N, M  = map(int, sys.stdin.readline().split())

n_list = {}
for _ in range(N):
    str_ = sys.stdin.readline().rstrip()   
    n_list[str_] = 1

for _ in range(M):
    ans = N
    str_ = sys.stdin.readline().rstrip().split(',') 
    
    for i in str_:
        if i in n_list:
            ans -= 1
            del n_list[i]

    print(len(n_list))