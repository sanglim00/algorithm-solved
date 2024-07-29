def solution(s):
    answer = True
    stack = []
    print(len(stack))
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack):
                now = stack.pop()
                if now != '(':
                    answer = False
                    break
            else:
                answer = False
                break
    
    return True if not len(stack) and answer else False