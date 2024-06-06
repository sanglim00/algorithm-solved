import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0
sum_ = 0
start, end = 0, 1

sum_ = arr[start]

while True:
    if sum_ < m:
        if end < n:
            sum_ += arr[end]
            end += 1
        else: 
            break
    elif sum_ > m:
        sum_ -= arr[start]
        start += 1
    else:
        ans += 1
        sum_ -= arr[start]
        start += 1
        
print(ans)
