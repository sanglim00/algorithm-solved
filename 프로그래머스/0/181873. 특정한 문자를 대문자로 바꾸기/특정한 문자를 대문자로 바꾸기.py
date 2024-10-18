def solution(my_string, alp):
    ans = ''
    for i in range(len(my_string)):
        if my_string[i] == alp:
            ans += my_string[i].upper()
        else:
            ans += my_string[i]
    return ans