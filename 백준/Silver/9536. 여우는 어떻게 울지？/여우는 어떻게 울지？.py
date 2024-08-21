import sys

N = int(sys.stdin.readline())
for _ in range(N):
    lst = []
    myDict = {}
    
    while True:
        str_ = sys.stdin.readline().rstrip()
        if str_ == 'what does the fox say?': break
        lst.append(str_)
    
    for i in range(1, len(lst)):
        sound = lst[i].split('goes')[1].strip()
        myDict[sound] = 1
    
    for i in lst[0].split(' '):
        if i not in myDict:
            print(i, end=' ')
    print()   