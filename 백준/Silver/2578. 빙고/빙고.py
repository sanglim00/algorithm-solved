graph_ = []
for _ in range(5):
    lst = list(map(int, input().split()))
    graph_.append(lst)

check = [[0 for _ in range(5)] for _ in range(5)]

def bingo(num):
    bingo_check = 0
    for i in range(5):
        for j in range(5):
            if graph_[i][j] == num:
                check[i][j] = 1

    for i in range(5):
        if (check[i][0] + check[i][1] + check[i][2] + check[i][3] + check[i][4]) == 5: bingo_check +=1
        if (check[0][i] + check[1][i] + check[2][i] + check[3][i] + check[4][i]) == 5: bingo_check +=1

    diagonal = check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4]
    diagonal2 = check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0]
    
    if diagonal == 5: bingo_check += 1
    if diagonal2 == 5: bingo_check += 1
    
    return bingo_check
    
ans = 0
stop = False
for _ in range(5):
    lst = list(map(int, input().split()))
    for i in lst:
        if stop: continue
        ans += 1
        if bingo(i) > 2: stop = True

print(ans)