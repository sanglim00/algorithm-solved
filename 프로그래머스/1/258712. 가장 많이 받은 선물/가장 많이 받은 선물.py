def solution(friends, gifts):
    
    arr = [[0 for j in range(len(friends))] for i in range(len(friends))]
    score = [0 for i in range(len(friends))]
    
    for i in range(len(gifts)):
        _from = gifts[i].split(' ')[0]
        _to = gifts[i].split(' ')[1]
        
        arr[friends.index(_from)][friends.index(_to)] += 1
        score[friends.index(_from)] += 1
        score[friends.index(_to)] -= 1

    ans = [0 for i in range(len(friends))]
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[i][j] > arr[j][i]:
                ans[i] += 1
            elif arr[i][j] < arr[j][i]:
                ans[j] += 1
            elif arr[i][j] == arr[j][i]:
                if score[i] > score[j]: ans[i] += 1
                elif score[j] > score[i]: ans[j] +=1

    return max(ans)