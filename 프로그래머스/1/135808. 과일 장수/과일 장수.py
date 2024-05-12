def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    score = score[0:len(score)-len(score)%m]
    
    i = 0
    while i+m <= len(score):
        minNum = min(score[i:i+m])
        answer+=minNum*m
        i +=m

        
        
    
    
    
    return answer