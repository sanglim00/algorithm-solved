def solution(s, n):
    answer = ''
    
    Upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']
    Lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    
    lst = list(s)
    
    for i in lst:
        if i == ' ':
            answer += ' '
            continue
        if i.isupper():
            now = 0
            for j in range(len(Upper)):
                if i == Upper[j]:
                    now = j
                    break
            answer += Upper[(j+n)%len(Upper)]   
        else:
            now = 0
            for j in range(len(Lower)):
                if i == Lower[j]:
                    now = j
                    break
            answer += Lower[(j+n)%len(Lower)]  
    return answer