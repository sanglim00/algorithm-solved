NUM = 5

graph_ = []
for _ in range(NUM):
    nums = list(input().rstrip().split())
    graph_.append(nums)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

mySet = set()
def DFS(v, str_):
    if len(str_) == 6:
        if str_ not in mySet: mySet.add(str_)
        return

    for i in range(4):
        ny, nx = v[0]+dy[i], v[1]+dx[i]
        if 0<=ny<NUM and 0<=nx<NUM:
            str_ += graph_[ny][nx]
            DFS((ny, nx), str_)
            str_ = str_[:-1]

for i in range(NUM):
    for j in range(NUM):
        str_ = graph_[i][j]
        DFS((i, j), str_)

print(len(mySet))