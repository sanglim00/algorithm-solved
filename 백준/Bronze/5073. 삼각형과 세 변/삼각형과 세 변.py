while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a, b, c = lst[0], lst[1], lst[2]
    if a == b == c == 0: break
    elif a+b <= c: print('Invalid')
    elif a == b == c: print('Equilateral')
    elif a != b != c: print('Scalene')
    elif a == b or b == c or a == c: print('Isosceles')