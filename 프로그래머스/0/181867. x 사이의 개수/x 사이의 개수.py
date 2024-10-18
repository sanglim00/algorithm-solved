def solution(myString):
    answer = []
    now = 0
    for i in myString.split('x'):
        answer.append(len(i))
        
    return answer