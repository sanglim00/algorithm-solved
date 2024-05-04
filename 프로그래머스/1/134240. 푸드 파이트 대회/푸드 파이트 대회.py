def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        if food[i] % 2 == 1:
            food[i] = food[i] - 1
        for j in range(food[i]//2):
            answer += str(i)
    
    answer += '0'
    
    for i in range(len(answer)-2, -1, -1):
        answer += answer[i]
    
    return answer