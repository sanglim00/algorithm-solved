graph_ = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph_[i][j] = 1

ans = 0
for i in range(101):
    for j in range(101):
        if graph_[i][j]: ans += 1
print(ans)