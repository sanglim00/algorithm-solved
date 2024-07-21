import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

ans = len(nums)
for i in nums:
    if i == 1:
        ans -= 1
    for j in range(2, i):
        if i % j == 0:
            ans -= 1
            break
    
print(ans)