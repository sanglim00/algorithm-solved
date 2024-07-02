import sys

stack_ = []
N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    if stack_ and num == 0:
        stack_.pop()
    else:
        stack_.append(num)

print(sum(stack_))

