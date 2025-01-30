N = int(input())
mySet = {'1', '2', '3', '5', '6', '8', '9', '0'}
for i in range(N, 0, -1):
    check = True
    for j in mySet:
        if j in str(i):
            check = False
            break
    
    if check: 
        print(i)
        break