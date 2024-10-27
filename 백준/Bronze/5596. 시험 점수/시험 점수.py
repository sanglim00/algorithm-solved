MK = list(map(int, input().split()))
MS = list(map(int, input().split()))

print(max(sum(MK), sum(MS)) if sum(MK) != sum(MS) else sum(MK))