one = int(input())
two = int(input())
three = int(input())

if one == two == three == 60:
    print('Equilateral')
elif one+two+three != 180:
    print('Error')
elif one == two or two == three or one == three:
    print('Isosceles')
elif one != two != three:
    print('Scalene')