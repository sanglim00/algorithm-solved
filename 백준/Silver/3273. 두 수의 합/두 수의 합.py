import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

lst.sort()
i, j = 0, len(lst)-1

ans = 0
while i < j:
    if lst[i] + lst[j] == m:
        ans +=1
        i+=1
        j-=1
    elif lst[i] + lst[j] > m:
        j-=1
    else:
        i+=1
    

print(ans)