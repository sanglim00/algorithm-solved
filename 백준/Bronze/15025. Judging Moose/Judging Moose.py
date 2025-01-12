A, B = map(int, input().split())
if A == B and A != 0:
    print(f"Even {A+B}")
elif A > B or A < B:
    print(f"Odd {max(A, B)*2}")
else:
    print("Not a moose")