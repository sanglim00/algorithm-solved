while True:
    A, B = map(int, input().split())
    if A==B==0: break

    if A < B and B % A == 0:
        print('factor')
    elif A > B and A % B ==0:
        print('multiple')
    else:
        print('neither')