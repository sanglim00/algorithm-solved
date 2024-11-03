N = int(input())

mySet = {
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
}

ans = 'No'
for _ in range(N):
    str_ = input().rstrip()
    if str_ not in mySet: ans = "Yes"
print(ans)