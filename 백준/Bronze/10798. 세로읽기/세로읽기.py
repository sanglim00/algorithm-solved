import sys

lst = [[' ' for _ in range(15)] for _ in range(5)]

for i in range(5):
    line = sys.stdin.readline().strip()
    _len = len(line)
    for j in range(_len):
        lst[i][j] = line[j]
    
ans = ''
for i in range(15):
    for j in range(5):
        ans += lst[j][i].strip()

print(ans)

