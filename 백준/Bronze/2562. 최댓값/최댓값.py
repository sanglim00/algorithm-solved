import sys

maxNum = 0
ans = 0

for i in range(1, 10):
    check = int(sys.stdin.readline())
    if maxNum < check : 
        maxNum= check
        ans = i

print(maxNum)
print(ans)