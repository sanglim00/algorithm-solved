N = int(input())

friends = []
for _ in range(N):
    f = list(input().split(' '))
    friends.append(f)

friends.sort(key=lambda x: (int(x[-1]), int(x[-2]), int(x[-3])))
print(friends[-1][0])
print(friends[0][0])