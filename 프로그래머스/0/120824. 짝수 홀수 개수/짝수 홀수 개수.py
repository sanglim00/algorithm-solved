def solution(num_list):
    
    a, b = 0, 0
    for i in num_list:
        if i % 2:
            b += 1
        else:
            a += 1
    answer = [a, b]           
    return answer