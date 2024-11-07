def solution(n, lost, reserve):
    
    res_, lost_ = [], []
    for i in lost:
        if i not in reserve: lost_.append(i)
    for i in reserve:
        if i not in lost: res_.append(i)
    
        
    answer = n - len(lost_)
    lost_.sort()
    res_.sort()
    
    myDict = dict()
    for i in res_: myDict[i] = 1
    
    for i in lost_:
        for j in (-1, 1):
            now = i+j
            if now in myDict and myDict[now]:
                answer += 1
                myDict[now] = 0
                break
    
    return answer