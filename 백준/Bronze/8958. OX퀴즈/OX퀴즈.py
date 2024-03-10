import sys

num = int(sys.stdin.readline())

for i in range(num):
    string = sys.stdin.readline()
    check = 1
    ans = 0

    for j in range(1, len(string)+1):
        if string[j-1] == 'O':
            ans += check
            check +=1
        else:
            check = 1
    
    print(ans)

    
