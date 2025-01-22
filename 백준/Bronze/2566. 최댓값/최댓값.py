max_ = 0
idx_i, idx_j = 0, 0
for i in range(9):
    lst= list(map(int, input().split()))
    for j in range(9):
        if max_ < lst[j]:
            idx_i, idx_j, max_ = i, j, lst[j]

print(max_)
print(idx_i+1, idx_j+1)