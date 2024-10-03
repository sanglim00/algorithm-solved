import sys

N = int(sys.stdin.readline())
words = {}

for _ in range(N):
    str_ = list(sys.stdin.readline().rstrip())
    str_.sort()
    str_ = ''.join(str_)
    if str_ in words: words[str_] += 1
    else: words[str_] = 1

print(len(words))