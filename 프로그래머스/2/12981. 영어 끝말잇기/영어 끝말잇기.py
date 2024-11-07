def solution(n, words):
    answer = []
    
    myDict = dict()
    for i in words: myDict[i] = 1
    myDict[words[0]] = 0
    
    now = words[0]
    idx = tern = 1
    
    check = False
    for i in range(1, len(words)):
        if idx == n:
            idx = 0
            tern += 1
        idx += 1
        if now[-1] == words[i][0] and myDict[words[i]]:
            myDict[words[i]] = 0
            now = words[i]
        else:
            check = True
        if check:
            answer.append(idx)
            answer.append(tern)
            break
        
    if not answer: answer = [0, 0]
    return answer