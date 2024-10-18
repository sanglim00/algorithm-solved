N = int(input())
graph_r, graph_c = [], [[] for _ in range(N)]

for _ in range(N):
    row = input().rstrip()
    graph_r.append(row.split('X'))
    for i in range(N): graph_c[i].append(list(row)[i-N])

r_cnt, c_cnt = 0, 0
for i in graph_r:
    for j in i:
        if len(j) > 1:
            r_cnt += 1

for i in range(N):
    now = ''.join(graph_c[i]).split('X')
    for j in now:
        if len(j) > 1:
            c_cnt += 1

print(r_cnt, c_cnt)