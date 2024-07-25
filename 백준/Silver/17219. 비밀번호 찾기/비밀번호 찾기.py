import sys

N, M = map(int, sys.stdin.readline().split())
myDict = {}

for _ in range(N):
    url, pw = sys.stdin.readline().split()
    myDict[url] = pw

for _ in range(M):
    url = sys.stdin.readline().rstrip()
    print(myDict[url])
