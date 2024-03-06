def solution(bandage, health, attacks):
    answer = health
    idx = 1 
    check = 0

    for i in range(1, attacks[-1][0]+1):
        for j in attacks:
            if idx == j[0]:
                answer -= j[1]
                check = 0
                idx += 1
                break
        if i == idx:
            idx += 1
            answer += bandage[1]
            check += 1
            if check == bandage[0]:
                answer += bandage[2]
                check = 0
        if answer > health:
            answer = health
        if answer < 1:
            return -1
            
    return answer