import sys

N = int(sys.stdin.readline())
lst = [-1 for _ in range(21)]
lst[0] = 0
lst[1] = 1

if N < 2: 
    print(N)
    exit()
for i in range(2, 21):
    lst[i] = lst[i-1] + lst[i-2]
    if i == N: 
        print(lst[i])
        break