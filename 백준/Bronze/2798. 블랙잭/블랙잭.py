import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

combi = list(combinations(cards, 3))
max_ = 0

for i in combi:
    if sum(i) <= M:
        max_ = max(max_, sum(i))

print(max_)