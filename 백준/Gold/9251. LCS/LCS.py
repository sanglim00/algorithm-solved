import sys
sys.setrecursionlimit(10000)

MAX = 1001

def LCS(str1, str2, m, n):
    if m <= 0 or n <= 0: return 0

    if arr[m][n] < 0:
        if str1[m-1] == str2[n-1]:
            arr[m][n] = LCS(str1, str2, m-1, n-1) + 1
        else:
            one = LCS(str1, str2, m-1, n)
            two = LCS(str1, str2, m, n-1)
            arr[m][n] = max(one, two)
    return arr[m][n]

arr = [[-1 for _ in range(MAX)] for _ in range(MAX)]

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
m, n = len(str1), len(str2)

print(LCS(str1, str2, m, n))