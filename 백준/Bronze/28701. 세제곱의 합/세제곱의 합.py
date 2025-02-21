N = int(input())

ans = 0
ans2 = 0
ans3 = 0
for i in range(1, N+1): 
    ans += i
    ans2 += i
    ans3 += i**3

print(ans)
print(ans2*ans2)
print(ans3)