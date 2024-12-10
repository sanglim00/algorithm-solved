import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)

vistied = [0 for _ in range(n)]


mySet = set()
def backtracking(idx, new_num):
    global mySet, vistied

    if idx == k:
        mySet.add(new_num)
        return 

    for i in range(n):
        if vistied[i]: continue
        vistied[i] = 1
        now_len = len(str(num_list[i]))
        now = str(num_list[i])
        new_num += now
        backtracking(idx+1, new_num)
        new_num = new_num[:-now_len]
        vistied[i] = 0

backtracking(0, '')
print(len(mySet))