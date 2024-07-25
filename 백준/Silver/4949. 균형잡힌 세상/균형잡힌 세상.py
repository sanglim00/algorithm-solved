import sys

while True:
    str_ = sys.stdin.readline().rstrip()
    if str_ == '.': break
    
    check = True
    stack = []

    for i in str_:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                check = False
                break
            now = stack.pop()
            if now != '(':
                check = False
                break
        elif i == ']':
            if len(stack) == 0:
                check = False
                break
            now = stack.pop()
            if now != '[':
                check = False
                break

    if check and len(stack) == 0:
        print('yes')
    else:
        print('no')