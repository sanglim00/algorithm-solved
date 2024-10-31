ansIdx = ansSum = 0

for i in range(1, 6):
    sum_ = sum(list(map(int, input().split())))
    if sum_ > ansSum:
        ansSum = sum_
        ansIdx = i

print(ansIdx, ansSum)