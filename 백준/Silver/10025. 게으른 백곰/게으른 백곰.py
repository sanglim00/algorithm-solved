import sys

MAX = 4000001
arr = [0 for i in range(MAX)]
 
n, k = map(int, sys.stdin.readline().split())

for i in range(n):
    g, x = map(int, sys.stdin.readline().split())
    arr[x] = g

max = 0

for i in range(0, 2*k+1):
    max += arr[i]

sum = max
for i in range(k+1, len(arr)-k):
    sum = sum-arr[i-k-1]+arr[i+k]
    if max < sum:
        max = sum

print(max)