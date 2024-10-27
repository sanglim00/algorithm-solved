def solution(binomial):
    answer = 0
    idx = 0
    while True:
        if binomial[idx] == '+':
            answer = int(binomial[:idx])+int(binomial[idx+1:])
            break
        elif binomial[idx] == '-':
            answer = int(binomial[:idx])-int(binomial[idx+1:])
            break
        elif binomial[idx] == '*':
            answer = int(binomial[:idx])*int(binomial[idx+1:])
            break
        idx += 1
    return answer