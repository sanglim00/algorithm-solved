import sys
from collections import Counter

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)

lst.sort()
check = Counter(lst).most_common()[:2]

print(round(sum(lst)/len(lst)))
print(lst[int(len(lst)/2)])
print(check[1][0] if len(check) == 2 and check[1][1] == check[0][1] else check[0][0])
print(max(lst)-min(lst))