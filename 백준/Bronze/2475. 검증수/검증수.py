import sys

lst = list(map(int, sys.stdin.readline().split()))
sum_ = 0
for i in lst:
    sum_ += i*i
sum_ %= 10

print(sum_)