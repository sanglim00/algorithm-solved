import sys

K, N = map(int, sys.stdin.readline().split())
lst = []
for _ in range(K):
    num = int(sys.stdin.readline())
    lst.append(num)

start, end = 1, max(lst)
check = 0

while start <= end :
    mid = (start+end)//2
    ans = 0
    for i in lst: ans += i//mid
    if ans >= N: 
        check = mid
        start = mid+1
    else:
        end = mid-1

print(check)