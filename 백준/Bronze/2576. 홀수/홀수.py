import sys

lst = []
min_ = 100
for _ in range(7):
    num = int(sys.stdin.readline())
    if num % 2 == 1:
        lst.append(num)
        min_ = min(min_, num)

if min_ != 100: print(sum(lst))
print(min_ if min_ != 100 else -1)