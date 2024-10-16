lst = list(map(int, input().split()))
lst.sort()
a, b, c = lst[0], lst[1], lst[2]

if a == b == c: print(a+b+c)
elif a + b > c: print(a+b+c)
else: print(a+b+(a+b-1))