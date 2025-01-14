T = int(input())
for _ in range(T):
    A, B = input().rstrip().split()
    print("OK" if A == B else "ERROR")