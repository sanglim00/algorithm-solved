import sys

R, C = map(int, sys.stdin.readline().split())
graph_ = [sys.stdin.readline().rstrip() for _ in range(R)]

px = [-1, 1, 0, 0]
py = [0, 0, -1, 1]

ans = 1

def DFS(y, x, visited_bitmask, path_length):
    global ans
    ans = max(ans, path_length)

    for i in range(4):
        ny, nx = y + py[i], x + px[i]
        if 0 <= ny < R and 0 <= nx < C:
            char_index = ord(graph_[ny][nx]) - ord('A')
            if not (visited_bitmask & (1 << char_index)): 
                DFS(ny, nx, visited_bitmask | (1 << char_index), path_length + 1)


DFS(0, 0, 1 << (ord(graph_[0][0]) - ord('A')), 1)
print(ans)