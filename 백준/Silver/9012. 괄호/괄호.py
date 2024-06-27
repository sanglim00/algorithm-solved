import sys

T = int(sys.stdin.readline())
for i in range(T):
    stack_ = []
    ans = True
    PS = sys.stdin.readline().strip()

    for j in PS:
        if j == "(": stack_.append(j)
        else:
            if stack_: stack_.pop()
            else:
                ans = False
                break
    print("YES" if not stack_ and ans else "NO")
    