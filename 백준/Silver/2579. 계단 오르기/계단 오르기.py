import sys

N = int(sys.stdin.readline())
score = []

for _ in range(N):
    num = int(sys.stdin.readline())
    score.append(num)

if N > 3:
    dp = [0 for _ in range(300+1)]
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0]+score[2], score[1]+score[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2], dp[i-3]+score[i-1])+score[i]
    print(dp[N-1])
    
elif N == 3:
    print(max(score[0]+score[2], score[1]+score[2]))
    
else:
    print(sum(score))