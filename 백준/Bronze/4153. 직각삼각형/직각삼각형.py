import sys
from math import sqrt

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0: break

    lst = [a, b, c]
    lst.sort()
    
    if (lst[0]**2)+(lst[1]**2) == lst[2]**2:
        print('right')
    else:
        print('wrong')