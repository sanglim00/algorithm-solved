N = int(input())

graph_ = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS': 0}
for _ in range(N):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        graph_['AXIS'] += 1
    elif x > 0 and y > 0:
        graph_['Q1'] += 1
    elif x < 0 and y > 0:
        graph_['Q2'] += 1
    elif x < 0 and y < 0:
        graph_['Q3'] += 1
    elif x > 0 and y < 0:
        graph_['Q4'] += 1

for k, v in graph_.items():
    print(f"{k}: {v}")