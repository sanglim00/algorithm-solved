import sys

chess = []
for _ in range(8):
    row = list(sys.stdin.readline().rstrip())
    chess.append(row)

check = []
for i in range(8):
    if i % 2 == 0: check.append([0, 1, 0, 1, 0, 1, 0, 1])
    else: check.append([1, 0, 1, 0, 1, 0, 1, 0])

ans = 0
for i in range(8):
    for j in range(len(check[i])):
        if check[i][j] == 0 and chess[i][j] == 'F':
            ans += 1

print(ans)