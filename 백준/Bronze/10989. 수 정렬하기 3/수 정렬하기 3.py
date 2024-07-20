import sys

N = int(sys.stdin.readline())
lst = [0 for _ in range(10000+1)]
for _ in range(N):
    num = int(sys.stdin.readline())
    lst[num] += 1

for i in range(len(lst)): 
    check = lst[i]
    while check:
        print(i)
        check -=1