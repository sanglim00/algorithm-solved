import sys

S = sys.stdin.readline().strip()
T = list(sys.stdin.readline().strip())

idx = len(T)-1

while len(S) != len(T):
    check = True if T[idx] == 'B' else False
    T.pop()
    idx -= 1
    if check: T.reverse()

print(1 if S ==''.join(T) else 0)