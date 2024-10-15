import sys

N, M = map(int, sys.stdin.readline().split())
lst = [i for i in range(1, N+1)]
lst.insert(0, 0)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start == end: continue
    arr = []
    for i in range(start, end+1):
        arr.append(lst[i])

    arr.reverse()
    idx = 0
    
    for i in range(start, end+1):
        lst[i] = arr[idx]
        idx +=1

for i in range(1, N+1): print(lst[i], end=' ')
print()