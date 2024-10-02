def solution(k, tangerine):
    answer = 0
    
    myDict = {}
    for i in tangerine:
        if i not in myDict: myDict[i] = 1
        else: myDict[i] += 1
        
    arr = sorted(list(map(int, myDict.values())))
    _sum, idx = 0, len(arr) - 1

    while _sum < k :
        _sum += arr[idx]
        idx -=1
        answer += 1
    
    return answer