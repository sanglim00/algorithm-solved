import sys

string = sys.stdin.readline().strip()
i= 0
j= len(string)-1
check = 1

while i != j:
    if i-j == 1:
        break
    if string[i] != string[j]:
        check = 0
        break
    else:
        i +=1
        j -=1

print(check)