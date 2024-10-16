import sys
from itertools import permutations

N = int(sys.stdin.readline())
lst = [i for i in range(1, N+1)]

for i in permutations(lst, N):
    for j in i:
        print(j, end=' ')
    print()