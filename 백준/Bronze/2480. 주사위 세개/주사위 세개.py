import sys

a, b, c = map(int, sys.stdin.readline().split())

if a==b and b==c and a==c:
    print(10000+a*1000)
elif (a ==b)or (a==c):
    print(1000+ a*100)
elif b==c:
    print(1000+ b*100)
else:
    print(max(a, max(b, c))*100)