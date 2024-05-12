def solution(s):
    answer = []
    
    myDict = {}
    
    for i in range(len(s)):
        if s[i] in myDict:
            answer.append(i-myDict[s[i]])
            myDict[s[i]] = i
        else:
            myDict[s[i]] = i
            answer.append(-1)
        
    return answer