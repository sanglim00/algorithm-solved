import sys

MAX = 10000
arr = [0 for _ in range(MAX)]

for i in range(1, len(arr)):
    if i%10 == i:
        arr[i+i] = -1
    else:
        idx = i
        i = str(i)
        for j in range(len(i)):
            idx += int(i[j])
        if idx < 10000:
            arr[idx] = -1
    if arr[int(i)] == 0:
        arr[int(i)] = int(i)

for i in range(1, len(arr)):
    if arr[i] != -1:
        print(arr[i])