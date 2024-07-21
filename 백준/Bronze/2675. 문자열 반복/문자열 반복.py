import sys

N = int(sys.stdin.readline())
for _ in range(N):
    num, str_ = sys.stdin.readline().split()
    for i in range(len(str_)):
        print(str_[i]* int(num), end='')
    print()
