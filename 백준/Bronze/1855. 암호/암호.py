K = int(input())
key = input().rstrip()

graph = []
i, j = 0, K
now = True
while j <= len(key):
    if now: graph.append(list(key[i:j]))
    else: graph.append(list(key[i:j][::-1]))
    i = j
    j += K
    now = not now

ans = ''
for i in range(len(graph[0])):
    for j in range(len(graph)):
        ans += graph[j][i]
print(ans)