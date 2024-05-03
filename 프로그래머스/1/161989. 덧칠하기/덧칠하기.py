def solution(n, m, section):
    answer = 0
    
    lst = [1 for _ in range(n)]
    for i in section: lst[i-1] = 0
    
    idx = 0
    
    while idx != n:
        if lst[idx] == 0:
            answer += 1
            for i in range(m):
                if idx < n:
                    lst[idx] = 1
                    idx += 1
                else:
                    ldx = n - idx
        else:
            idx += 1
        
    return answer