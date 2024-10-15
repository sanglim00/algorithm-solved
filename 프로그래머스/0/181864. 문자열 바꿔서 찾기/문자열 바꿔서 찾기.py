def solution(myString, pat):
    answer = 0
    str_ = ''
    for i in range(len(myString)):
        if myString[i] == 'A': str_ += 'B'
        else: str_ +='A'
        
    return 1 if pat in str_ else 0