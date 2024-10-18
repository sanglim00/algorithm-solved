def solution(s):
    answer = ''
    now = True
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            now = True
        elif now: 
            answer += s[i].upper()
            now = False
        else:
            answer += s[i].lower()
    return answer