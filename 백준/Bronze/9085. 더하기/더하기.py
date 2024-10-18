T = int(input())
for _ in range(T):
    num = int(input())
    lst = list(map(int, input().split()))
    print(sum(lst))